import os
import argparse
load_dir = ['sac', 
            'sac_0', 
            'ppo_0',
            'td3_0']
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--route1', type=int, default = 0)
parser.add_argument('--route2', type=int, default = 1)
parser.add_argument('--scenario1', type=int, default = 1)
parser.add_argument('--scenario2', type=int, default = 2)
args = parser.parse_args()

# for scenario in range(args.scenario1, args.scenario2):
#     for _ in range(6):
#         for route in range(args.route1, args.route2):
#             os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode train_scenario --policy1 sac --load1 sac --route1 {route} --scenario1 {scenario}")
            
# for scenario in range(args.scenario1, args.scenario2):
#     for _ in range(6):
#         for route in range(args.route1, args.route2): 
#             os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode eval --policy1 sac --load1 sac_0 --route1 {route} --scenario1 {scenario}")
#             os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode eval --policy1 ppo --load1 ppo_0 --route1 {route} --scenario1 {scenario}")
#             os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode eval --policy1 td3 --load1 td3_0 --route1 {route} --scenario1 {scenario}")

for scenario in range(args.scenario1, args.scenario2):
    for _ in range(1):
        for route in range(args.route1, args.route2): 
            os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode eval --policy1 sac --load1 advsim --route1 {route} --scenario1 {scenario}")
#             os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode eval --policy1 sac --load1 advtraj --route1 {route} --scenario1 {scenario}")
#             os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode eval --policy1 sac --load1 cc --route1 {route} --scenario1 {scenario}")
#             os.system(f"DISPLAY=:9 python scripts/run.py --agent_cfg=safe_rl.yaml --scenario_cfg=scenic.yaml --num_scenario 1 --mode eval --policy1 sac --load1 lc --route1 {route} --scenario1 {scenario}")
