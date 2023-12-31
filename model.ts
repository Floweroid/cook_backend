export type Difficulty = '简单' | '普通' | '困难'

export interface RecipeItem {
  /**
   * 菜名
   */
  name: string
  /**
   * 链接
   */
  link?: string
  /**
   * BiliBili video id
   */
  bv?: string
  /**
   * 材料
   */
  stuff: string[]
  /**
   * 根据材料生成
   */
  emojis?: string[]
  /**
   * 难度
   */
  difficulty?: Difficulty | ''
  /**
   * 标签
   */
  tags?: string[]
  /**
   * 方式
   */
  methods?: ('炒' | '煎' | '烘' | '炸')[]
  /**
   * 工具
   */
  tools: string[]
}

export type Recipes = RecipeItem[]

export interface StuffItem {
  /**
   * 食材名称
   */
  name: string
  /**
   * 例如：🥔
   */
  emoji: string
  /**
   * 图片链接
   */
  image?: string
  /**
   * 别名，譬如：西红柿/番茄
   */
  alias?: string
  /**
   * 图标名称
   */
  icon?: string
  /**
   * 显示标签
   */
  label?: string
}

export interface Cookbook {
  /**
   * 菜谱 ID，自定义，唯一标识符
   */
  id: string
  cover?: string
  /**
   * 菜谱名称
   */
  title: string
  description: string
  author: string | string[]
  /**
   * 菜谱
   */
  recipes: Recipes

  createdAt: string
  updatedAt: string
}


/**
 * 素菜
 */
export const vegetable: StuffItem[] = [
  {
    name: '土豆',
    emoji: '🥔',
  },
  {
    name: '胡萝卜',
    emoji: '🥕',
  },
  {
    name: '花菜',
    emoji: '🥦',
  },
  {
    name: '白萝卜',
    emoji: '🥣',
  },
  {
    name: '西葫芦',
    emoji: '🥒',
  },
  {
    name: '番茄',
    emoji: '🍅',
    alias: '西红柿',
  },
  {
    name: '芹菜',
    emoji: '🥬',
  },
  {
    name: '黄瓜',
    emoji: '🥒',
  },
  {
    name: '洋葱',
    emoji: '🧅',
  },
  {
    name: '莴笋',
    emoji: '🎍',
  },
  {
    name: '菌菇',
    emoji: '🍄',
  },
  {
    name: '茄子',
    emoji: '🍆',
  },
  {
    name: '豆腐',
    emoji: '🍲',
  },
  {
    name: '包菜',
    emoji: '🥗',
  },
  {
    name: '白菜',
    emoji: '🥬',
  },
]

/**
 * 荤菜
 */
export const meat: StuffItem[] = [
  {
    name: '午餐肉',
    emoji: '🥓',
  },
  {
    name: '香肠',
    emoji: '🌭',
  },
  {
    name: '腊肠',
    emoji: '🌭',
  },
  {
    name: '鸡肉',
    emoji: '🐤',
  },
  {
    name: '猪肉',
    emoji: '🐷',
  },
  {
    name: '鸡蛋',
    emoji: '🥚',
  },
  {
    name: '虾',
    emoji: '🦐',
  },
  {
    name: '牛肉',
    emoji: '🐮',
  },
  {
    name: '骨头',
    emoji: '🦴',
  },
  {
    name: '鱼（Todo）',
    emoji: '🐟',
  },
]

/**
 * 主食
 */
export const staple: StuffItem[] = [
  {
    name: '面食',
    emoji: '🍝',
  },
  {
    name: '面包',
    emoji: '🍞',
  },
  {
    name: '米',
    emoji: '🍚',
  },
  {
    name: '方便面',
    emoji: '🍜',
  },
]

export const tools: StuffItem[] = [
  {
    name: '烤箱',
    emoji: '',
    icon: 'i-mdi-toaster-oven',
  },
  {
    name: '空气炸锅',
    emoji: '',
    icon: 'i-fe-frying-pan',
  },
  {
    name: '微波炉',
    emoji: '',
    icon: 'i-ic-outline-microwave',
  },
  {
    name: '电饭煲',
    emoji: '',
    icon: 'i-gg-smart-home-cooker',
  },
  {
    label: '一口能炒又能煮的大锅',
    name: '一口大锅',
    emoji: '',
    icon: 'i-mdi-pot-steam-outline',
  },
]
