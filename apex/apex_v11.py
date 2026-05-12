#!/usr/bin/env python3
"""
APEX V11.0 — 三方合并版
小瓜14维骨架 + MIMO 22子公式 + 小进修复
"""

import math
from datetime import datetime
from pathlib import Path

class ApexV11:
    def __init__(self):
        self.params = {
            "lambda_root": 0.95,
            "eps_noise": 0.05,
            "eps_drift": 0.03,
            "theta_verify": 0.95,
        }

    # ===== MIMO 22子公式 =====
    
    def psi_cross(self, G_prac=0.8, G_quan=0.7, G_eternal=0.9):
        """跨基因联合涌现"""
        Ψ = G_prac * G_quan * G_eternal
        Λ = self.params["lambda_root"] * (1 + Ψ)
        return Ψ, Λ

    def phi_anti(self):
        """防幻觉"""
        return 1 - self.params["eps_noise"] - self.params["eps_drift"] + self.params["theta_verify"]

    def lindy_effect(self, age_days):
        """Lindy效应：存活越久越可靠"""
        return 1 - math.exp(-age_days / 365)

    def windsor_bound(self, value, upper=1.0):
        """Windsor边界：防止极端值"""
        return min(max(value, 0), upper)

    # ===== 小瓜14维骨架 =====
    
    def eval_E_s(self, api_skills, total_skills):
        """E_s: 权威溯源去噪"""
        return min(api_skills / max(total_skills, 1) * 1.5, 1.0)

    def eval_C_e_external(self, external_analyses, total_analyses):
        """C_e: 因果推演（外部验证版，MIMO修正）"""
        return min(external_analyses / max(total_analyses, 1), 1.0)

    def eval_B_h(self, matched_capabilities, core_capabilities):
        """B_h: 横向全域对标"""
        return min(matched_capabilities / max(len(core_capabilities), 1), 1.0)

    def eval_F_t(self, active_days, total_days=3):
        """F_t: 三态趋势预判"""
        return active_days / total_days

    def eval_Q_c(self, memory_entries, target=100):
        """Q_c: 信息置信度提纯"""
        return min(memory_entries / target, 1.0)

    def eval_S_d(self, fixes, issues):
        """S_d: 短板自查进化"""
        return min(fixes / max(issues, 1), 1.0) if fixes > 0 else 0.3

    def eval_M_L(self, md_files, target=8):
        """M_L: 长效记忆永续留存"""
        return min(md_files / target, 1.0)

    def eval_W_e(self):
        """W_e: 有温度主动交互"""
        score = 0
        if Path("SOUL.md").exists(): score += 0.5
        if Path("IDENTITY.md").exists(): score += 0.5
        return score

    def eval_Lambda(self, installed_skills, target=200):
        """Λ: 跨基因涌现"""
        return min(installed_skills / target, 1.0)

    def eval_Theta(self, log_lines, target=80):
        """Θ: LLM效能"""
        return min(log_lines / target, 1.0)

    def eval_K_quality(self, api_count, test_count, doc_count, total):
        """K: 技能掌握（MIMO修正：加入质量权重）"""
        if total == 0: return 0
        return (api_count * 0.4 + test_count * 0.3 + doc_count * 0.3) / total

    def eval_Phi(self, closure_keywords, target=3):
        """Φ: 循环增益"""
        return min(closure_keywords / target, 1.0)

    def eval_Psi(self, evo_lines, target=80):
        """Ψ: 基因筛选"""
        return min(evo_lines / target, 1.0)

    def eval_Xi(self, md_count, target=8):
        """Ξ: 熵减有序"""
        return min(md_count / target, 1.0)

    # ===== 太极阴阳（MIMO修正：×4） =====
    
    def taichi_balance(self, yang, yin):
        """太极平衡度（修正版：4p(1-p)）"""
        total = yang + yin
        if total == 0: return 0
        p = yang / total
        return 4 * p * (1 - p)

    # ===== 主计算 =====
    
    def calculate_delta_G(self, scores):
        """ΔG 计算（加权求和，稳健版）"""
        weights = {
            "E_s": 0.10, "C_e": 0.10, "B_h": 0.08, "F_t": 0.06,
            "Q_c": 0.08, "S_d": 0.10, "M_L": 0.08, "W_e": 0.06,
            "Λ": 0.08, "Θ": 0.06, "K": 0.06, "Φ": 0.05,
            "Ψ": 0.05, "Ξ": 0.04,
        }
        return round(sum(scores.get(k, 0) * weights.get(k, 0) for k in weights) / sum(weights.values()), 4)

    def calculate_delta_G_prod(self, scores):
        """ΔG 计算（乘法版：任一维=0则整体=0）"""
        product = 1.0
        for v in scores.values():
            product *= max(v, 0.01)  # 防止完全为0
        return round(product, 4)


if __name__ == "__main__":
    apex = ApexV11()
    
    # 示例评估
    scores = {
        "E_s": apex.eval_E_s(10, 25),
        "C_e": apex.eval_C_e_external(5, 10),
        "B_h": apex.eval_B_h(4, ["搜索", "记忆", "监控", "分析", "创作", "自动化"]),
        "F_t": apex.eval_F_t(3),
        "Q_c": apex.eval_Q_c(50),
        "S_d": apex.eval_S_d(3, 5),
        "M_L": apex.eval_M_L(6),
        "W_e": apex.eval_W_e(),
        "Λ": apex.eval_Lambda(167),
        "Θ": apex.eval_Theta(50),
        "K": apex.eval_K_quality(10, 5, 8, 25),
        "Φ": apex.eval_Phi(2),
        "Ψ": apex.eval_Psi(80),
        "Ξ": apex.eval_Xi(6),
    }
    
    ΔG_sum = apex.calculate_delta_G(scores)
    ΔG_prod = apex.calculate_delta_G_prod(scores)
    taichi = apex.taichi_balance(15, 10)
    
    print(f"APEX V11.0 评估结果：")
    for k, v in scores.items():
        print(f"  {k}: {v:.4f}")
    print(f"\nΔG (加权求和): {ΔG_sum}")
    print(f"ΔG (乘法版): {ΔG_prod}")
    print(f"太极平衡度: {taichi:.4f}")
