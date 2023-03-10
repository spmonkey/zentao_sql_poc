# 禅道系统权限绕过到SQL注入
> 漏洞描述

禅道是第一款国产的开源项目管理软件，它的核心管理思想基于敏捷方法 scrum，内置了产品管理和项目管理，同时又根据国内研发现状补充了测试管理、计划管理、发布管理、文档管理、事务管理等功能，在一个软件中就可以将软件研发中的需求、任务、bug、用例、计划、发布等要素有序地跟踪管理起来，完整地覆盖了项目管理的核心流程。 该漏洞是由于禅道项目管理系统权限认证存在缺陷导致，攻击者可利用该漏洞在未授权的情况下，通过权限绕过执行任意sql语句。

> 影响范围

|  禅道系统   | 影响版本  |
|  ----  | ----  |
| 开源版  | V17.4<=version<=V18.0.beta1 |
| 旗舰版  | V3.4<=version<=V4.0.beta1 |
| 企业版  | V7.4<=version<=V8.0.beta1 |

> 详情分析

查看分析文章：https://www.cnblogs.com/spmonkey/protected/p/17050708.html

## 漏洞分析仅供学习交流和思路分享，请勿⽤于⾮法⽤途。
