#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
水果 ID 卡批量保存脚本
使用方式：python3 save_fruits.py 'JSON 数据'
或直接粘贴 JSON 到 stdin
"""

import json
import sys
import os

OUTPUT_DIR = "/app/working/mydata/project/fruit-idcard"

def save_fruit(data):
    """单个水果保存到独立 JSON 文件"""
    fruit_id = data.get('id')
    if not fruit_id:
        print(f"⚠️ 跳过：缺少 id 字段")
        return False
    
    file_path = os.path.join(OUTPUT_DIR, f"{fruit_id}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ {fruit_id} ({data.get('name', 'unknown')})")
    return True

def main(json_data):
    """主函数"""
    # 确保目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 解析 JSON（支持数组或单对象）
    if isinstance(json_data, str):
        try:
            data_list = json.loads(json_data)
        except json.JSONDecodeError as e:
            print(f"❌ JSON 解析失败：{e}")
            return
    
    # 如果是单个对象，转为数组
    if isinstance(data_list, dict):
        data_list = [data_list]
    
    # 批量保存
    success_count = 0
    total_count = len(data_list)
    
    print(f"\n📦 开始保存 {total_count} 种水果...\n")
    
    for item in data_list:
        if save_fruit(item):
            success_count += 1
    
    print(f"\n{'='*50}")
    print(f"✅ 完成：{success_count}/{total_count} 种水果已保存")
    print(f"📁 保存路径：{OUTPUT_DIR}/")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 从命令行参数读取 JSON
        json_input = " ".join(sys.argv[1:])
    else:
        # 从 stdin 读取（支持管道）
        json_input = sys.stdin.read()
    
    main(json_input)
