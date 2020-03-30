{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'StationNode'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-c53132554a57>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mStationNode\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[1;33m*\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m# 코드를 추가하세요\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mcreate_subway_graph\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput_file\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;34m\"\"\"input_file에서 데이터를 읽어 와서 지하철 그래프를 리턴하는 함수\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'StationNode'"
     ]
    }
   ],
   "source": [
    "from StationNode import *\n",
    "\n",
    "# 코드를 추가하세요\n",
    "def create_subway_graph(input_file):\n",
    "    \"\"\"input_file에서 데이터를 읽어 와서 지하철 그래프를 리턴하는 함수\"\"\"\n",
    "    stations = {}  # 지하철 역 노드들을 담을 딕셔너리\n",
    "\n",
    "    # 파라미터로 받은 input_file 파일을 연다\n",
    "    with open(input_file) as stations_raw_file:\n",
    "        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다\n",
    "            previous_station = None  # 엣지를 저장하기 위한 도우미 변수. 현재 보고 있는 역 전 역을 저장한다\n",
    "            subway_line = line.strip().split(\"-\")  # 앞 뒤 띄어쓰기를 없애고 \"-\"를 기준점으로 데이터를 나눈다\n",
    "\n",
    "            for name in subway_line:\n",
    "                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기\n",
    "\n",
    "                # 지하철 역 이름이 이미 저장한 key 인지 확인\n",
    "                if station_name not in stations:\n",
    "                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고\n",
    "                    stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 인스턴스를 value로 저장한다\n",
    "\n",
    "                else:\n",
    "                    current_station = stations[station_name]  # 이미 저장한 역이면 stations에서 역 인스턴스를 갖고 온다\n",
    "\n",
    "                if previous_station is not None:\n",
    "                    current_station.add_connection(previous_station)  # 현재 역과 전 역의 엣지를 연결한다\n",
    "\n",
    "                previous_station = current_station  # 현재 역을 전 역으로 저장\n",
    "\n",
    "    return stations\n",
    "    \n",
    "    \n",
    "stations = create_subway_graph(\"./stations.txt\")  # stations.txt 파일로 그래프를 만든다\n",
    "\n",
    "# stations에 저장한 역 인접 역들 출력 (체점을 위해 역 이름 순서대로 출력)\n",
    "for station in sorted(stations.keys()):\n",
    "    print(stations[station])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
