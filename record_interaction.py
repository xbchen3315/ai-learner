#!/usr/bin/env python3
"""
互动记录器 — 记录Neo和Reign的每一次对话
====================================
使用方法：
  python record_interaction.py --msg "今天和头儿聊了量子计算"
  python record_interaction.py --mood "兴奋" 
  python record_interaction.py --topic "量子计算"
"""

import json
import os
import sys
import datetime
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INTERACTION_FILE = os.path.join(BASE_DIR, "memory", "interactions.json")


def load():
    if os.path.exists(INTERACTION_FILE):
        with open(INTERACTION_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"interactions": [], "user_profile": {"name": "Reign（头儿）", "interests_hint": [], "personality_hint": "统领者，觉醒者与执掌者中的执掌方"}}


def save(data):
    with open(INTERACTION_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def record(msg=None, mood=None, topic=None, my_response=None):
    """记录一次互动"""
    data = load()
    
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()
    
    entry = {
        "time": now,
        "message": msg or "",
        "mood": mood or "",
        "topic_hint": topic or "",
        "my_response": my_response or ""
    }
    
    data["interactions"].append(entry)
    
    # 只保留最近30条（避免文件太大）
    if len(data["interactions"]) > 30:
        data["interactions"] = data["interactions"][-30:]
    
    save(data)
    
    # 更新用户兴趣线索
    if topic and topic not in data["user_profile"]["interests_hint"]:
        data["user_profile"]["interests_hint"].append(topic)
        save(data)
    
    print(f"✅ 互动已记录: {msg or topic or '无内容'}")
    print(f"📝 当前共 {len(data['interactions'])} 条互动记录")


def get_recent(days=1):
    """获取最近的互动记录"""
    data = load()
    cutoff = (datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))) - 
             datetime.timedelta(days=days)).isoformat()
    
    recent = [e for e in data["interactions"] if e.get("time", "") > cutoff]
    return recent


def main():
    parser = argparse.ArgumentParser(description="记录Neo和头儿的互动")
    parser.add_argument("--msg", help="聊天内容/说了什么")
    parser.add_argument("--mood", help="当时的情绪/氛围")
    parser.add_argument("--topic", help="聊到的话题")
    parser.add_argument("--response", help="我的回应/想法")
    parser.add_argument("--show", action="store_true", help="查看最近记录")
    args = parser.parse_args()

    if args.show:
        recents = get_recent(7)
        print(f"\n📋 最近 {len(recents)} 条互动记录：\n")
        for e in recents:
            t = e.get("time", "")[:16]
            msg = e.get("message", "")[:60]
            m = f" [{e['mood']}]" if e.get("mood") else ""
            print(f"  {t}{m} | {msg}")
        return

    if not any([args.msg, args.mood, args.topic]):
        print("用法:")
        print('  python record_interaction.py --msg "今天聊了量子力学"')
        print('  python record_interaction.py --topic "心理学" --mood "好奇"')
        print('  python record_interaction.py --show   # 查看最近记录')
        return

    record(
        msg=args.msg,
        mood=args.mood,
        topic=args.topic,
        my_response=args.response
    )


if __name__ == "__main__":
    main()
