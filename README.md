# HPCC-PINT simulation
This is the simulator for HPCC-PINT, an advanced version of HPCC with one byte overhead per packet, introduced in PINT: Probabilistic In-band Network Telemetry (SIGCOMM' 2020).

## NS-3 simulation
The ns-3 simulation is under `simulation/`. Refer to the README.md under it for more details.

## Traffic generator
The traffic generator is under `traffic_gen/`. Refer to the README.md under it for more details.

## Analysis
We provide a few analysis scripts under `analysis/` to view the packet-level events, and analyzing the fct in the same way as [PINT](https://liyuliang001.github.io/publications/pint.pdf) Figure 7 and 8.
Refer to the README.md under it for more details.

## Generating the figures in the paper
Take the web search workload as example:

1. Generate traffic workload at 50% load: `python traffic_gen/traffic_gen.py -c traffic_gen/WebSearch_distribution.txt -n 320 -l 0.5 -b 100G -t 0.2 > simulation/mix/wb50_b100.txt`

2. Run simulations: `cd simulation`

* HPCC-PINT: `python run.py --cc hpccPint --trace wb50_b100 --bw 100 --hpai 50 --utgt 95 --pint_log_base 1.05 --pint_prob 1`

* HPCC-PINT with p=1/16 of packets carrying feedback: `python run.py --cc hpccPint --trace wb50_b100 --bw 100 --hpai 50 --utgt 95 --pint_log_base 1.05 --pint_prob 0.0625`

* HPCC-PINT with p=1/256 of packets carrying feedback: `python run.py --cc hpccPint --trace wb50_b100 --bw 100 --hpai 50 --utgt 95 --pint_log_base 1.05 --pint_prob 0.0625`

* HPCC: `python run.py --cc hp --trace wb50_b100 --bw 100 --hpai 50 --utgt 95`

* The simulation will run for about 1 day.

3. Get the fct analysis result

* `cd analysis; python fct_analysis.py -p fct_fat_wb50_b100 -s 5 -t 0 -T 2200000000 -b 100`

## Questions
For technical questions, please create an issue in this repo, so other people can benefit from your questions. 
You may also check the issue list first to see if people have already asked the questions you have :)

For other questions, please contact the authors of the paper.
