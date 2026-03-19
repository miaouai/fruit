# 🍊 水果闹 (NOW)

> **时令水果查询指南** - 了解中国境内每个月上市的新鲜水果

<div align="center">

![Project Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-blue)
[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-lightgrey)](https://miaouai.github.io/fruit/)

📅 按季节查询 | 🌏 覆盖全国产区 | 💡 营养小贴士

</div>

---

## 📖 项目简介

「水果闹」是一个致力于记录和展示中国境内不同月份应季水果的开源项目。通过本项目的数据，用户可以：

- 🗓️ **按月查询**：快速了解每个月有哪些水果正当季
- 🌏 **产地信息**：标注每个水果的主要产区
- 🥗 **健康饮食**：遵循自然规律，吃当季最好吃的水果
- 💰 **省钱攻略**：应季水果价格更实惠！

---

## 🚀 在线访问

- **GitHub Pages**: https://miaouai.github.io/fruit/
- **GitHub 仓库**: https://github.com/miaouai/fruit

---

## 🎨 功能预览

### 双栏交互设计

| 第一栏：当前应季 | 第二栏：月份查询 |
|----------------|----------------|
| 自动检测当前月份显示应季水果 | 1-12 月标签自由切换 |
| 点击直接查看水果详情 | 查看指定月份的水果列表 |

### 独立弹窗系统

- 🔍 **月份列表弹窗**：显示该月的所有应季水果
- 📋 **水果 ID 卡弹窗**：完整的水果信息档案
- ✅ **互不干扰**：关闭 ID 卡不影响月份列表显示

---

## 🛠️ 技术架构

### 整体架构图

```
┌─────────────────────────────────────────────────────────┐
│                    index.html                          │
│                   (单页应用入口)                        │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
┌───────────────┐         ┌──────────────────┐
│ fruit-list.json│         │  fruit-idcard/   │
│               │         │                  │
│ - 水果主索引    │         │  ├── watermelon.json│
│ - 上市月份范围  │         │  ├── strawberry.json│
│ - 水果名映射     │         │  ├── orange.json   │
└───────────────┘         │  └── ...          │
        │                 │     (详细档案库)    │
        └────────────────┬────────────────────┘
                         │
                ┌────────▼─────────┐
                │   JavaScript     │
                │  (动态加载渲染)    │
                └──────────────────┘
```

### 核心逻辑流程

```javascript
// 1. 加载主数据
fetch('fruit-list.json')
  → fruitsData (包含所有水果的 id/name/harvest_start/harvest_end)

// 2. 获取当前月份
getCurrentMonth() → month (1-12)

// 3. 筛选应季水果
isFruitInMonth(fruit, month):
  - 处理跨年情况 (如砂糖橘 12 月→次年 3 月)
  - 返回布尔值

// 4. 渲染第一栏 (当前应季)
filter(fruits, currentMonth) → renderGrid()

// 5. 点击月份标签
showMonthFruits(month) → filter → openModal()

// 6. 点击查看详情
showIdCard(fruitId) → fetch(`fruit-idcard/${fruitId}.json`) → renderIdCard()
```

---

## 📁 目录结构

```
fruit/
├── index.html              # 主页（GitHub Pages 入口）
├── README.md               # 项目说明文档
├── fruit-list.json         # 水果主索引数据
└── fruit-idcard/           # 水果详细信息目录
    ├── watermelon.json     # 西瓜档案
    ├── strawberry-dandong.json  # 丹东草莓档案
    ├── orange-nanchun.json      # 赣南脐橙档案
    └── ... (更多水果档案)
```

---

## 📊 数据格式说明

### `fruit-list.json` - 主索引

```json
{
  "fruits": [
    {
      "id": "watermelon",           // 唯一标识符，与 ID 卡文件名对应
      "name": "西瓜",                // 显示名称
      "harvest_start": 5,           // 开始上市月份 (1-12)
      "harvest_end": 9              // 结束上市月份 (1-12)
    }
  ]
}
```

### `fruit-idcard/{id}.json` - 详细档案

```json
{
  "id": "watermelon",
  "name": "西瓜",
  "classification": {               // 分类信息
    "科": "葫芦科",
    "属": "西瓜属",
    "type": "夏季消暑水果"
  },
  "origin_range": ["新疆", "宁夏"], // 产地列表
  "best_season": "6-8 月盛夏时节",   // 最佳品尝期
  "nutrition_per_100g": {          // 营养成分表
    "热量": "30kcal",
    "维生素 C": "8mg"
  },
  "benefits": ["消暑解渴", "利尿"], // 功效列表
  "tips": ["选拍打声音清脆的"]     // 食用小贴士
}
```

---

## 🎯 项目目的

### 核心价值

1. **科普教育**：帮助大众了解时令水果知识
2. **健康生活**：倡导顺应季节的饮食方式
3. **数据共享**：开放水果数据库供开发者使用
4. **社区共建**：欢迎大家补充完善本地特色水果

### 适用场景

- 🏪 **家庭采购**：知道什么时候买什么水果最新鲜
- 👨‍👩‍👧 **亲子教育**：教孩子认识四季变化与食物关系
- 🍳 **烹饪参考**：根据季节选择食材
- 📱 **开发练习**：学习 JSON 数据驱动的前端项目

---

## 🤝 如何贡献

欢迎为这个项目贡献你家乡的水果知识！

### 添加新水果

1. **Fork 本仓库**

2. **在主索引中添加条目** (`fruit-list.json`)
   ```json
   {"id": "your-fruit-name", "name": "你的水果", "harvest_start": 3, "harvest_end": 5}
   ```

3. **创建详细档案** (`fruit-idcard/your-fruit-name.json`)
   - 参照现有 JSON 模板
   - 填写完整信息

4. **提交 Pull Request**

### 修改现有数据

如果发现错误或不准确的地方，欢迎提 Issue 或 PR 修正！

---

## 📈 数据统计

| 指标 | 数值 |
|------|------|
| 🍎 已收录水果 | 63+ 种 |
| 🗺️ 覆盖省份 | 20+ 个 |
| 📆 月份完整性 | 12/12 |
| 🔄 更新频率 | 持续维护中 |

---

## 🎨 界面设计

### 色彩方案

- **主背景**: 紫罗兰渐变 `#667eea` → `#764ba2`
- **卡片**: 粉橙渐变 + 白色玻璃质感
- **文字**: 深灰 `#333` 保证可读性

### 交互动画

- ✨ 页面载入：渐入效果
- 🎯 悬停反馈：轻微缩放 + 阴影加深
- 📂 弹窗打开：缩放淡入
- 🔒 遮罩层：高斯模糊 backdrop-filter

### 响应式适配

- 📱 移动端：单列布局，触摸优化
- 💻 桌面端：双栏并排，网格布局
- 📐 断点：768px

---

## 📜 许可证

本项目采用 MIT 许可证，欢迎自由使用和分发。

---

## 👨‍💻 维护者

[@miaouai](https://github.com/miaouai)

如有问题或建议，欢迎提交 [Issue](https://github.com/miaouai/fruit/issues)

---

<div align="center">

**吃当季水果，享健康生活 🥬**

⭐ 如果这个项目对你有帮助，欢迎 Star 支持！

---

Made with ❤️ by [喵有爱](https://github.com/miaouai)

</div>
