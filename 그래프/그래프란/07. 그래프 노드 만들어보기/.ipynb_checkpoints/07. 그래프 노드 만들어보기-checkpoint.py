{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "UnicodeDecodeError",
     "evalue": "'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnicodeDecodeError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-67f52c9e14ba>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     30\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     31\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 32\u001b[1;33m \u001b[0mstations\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcreate_station_nodes\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"./stations.txt\"\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# stations.txt 파일로 그래프 노드들을 만든다\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     33\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     34\u001b[0m \u001b[1;31m# stations에 저장한 역들 이름 출력 (체점을 위해 역 이름 순서대로 출력)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-4-67f52c9e14ba>\u001b[0m in \u001b[0;36mcreate_station_nodes\u001b[1;34m(input_file)\u001b[0m\n\u001b[0;32m     14\u001b[0m     \u001b[1;31m# 파라미터로 받은 input_file 파일을 연다\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m     \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput_file\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mstations_raw_file\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 16\u001b[1;33m         \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mstations_raw_file\u001b[0m\u001b[1;33m:\u001b[0m  \u001b[1;31m# 파일을 한 줄씩 받아온다\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     17\u001b[0m             \u001b[0msubway_line\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mline\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstrip\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"-\"\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# 앞 뒤 띄어쓰기를 없애고 \"-\"를 기준점으로 데이터를 나눈다\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     18\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mUnicodeDecodeError\u001b[0m: 'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence"
     ]
    }
   ],
   "source": [
    "## 07. 그래프 노드 만들어보기\n",
    "\n",
    "class StationNode:\n",
    "    \"\"\"간단한 지하철 역 노드 클래스\"\"\"\n",
    "    def __init__(self, station_name):\n",
    "        self.station_name = station_name\n",
    "        \n",
    "\n",
    "\n",
    "def create_station_nodes(input_file):\n",
    "    \"\"\"input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수\"\"\"\n",
    "    stations = {}  # 지하철 역 노드들을 담을 딕셔너리\n",
    "\n",
    "    # 파라미터로 받은 input_file 파일을 연다\n",
    "    with open(input_file) as stations_raw_file:\n",
    "        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다\n",
    "            subway_line = line.strip().split(\"-\")  # 앞 뒤 띄어쓰기를 없애고 \"-\"를 기준점으로 데이터를 나눈다\n",
    "\n",
    "            for name in subway_line:\n",
    "                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기\n",
    "\n",
    "                # 코드를 쓰세요\n",
    "                # 지하철 역 이름이 이미 저장한 key 인지 확인\n",
    "                if station_name not in stations:\n",
    "                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고\n",
    "                    stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다\n",
    "\n",
    "    return stations\n",
    "\n",
    "\n",
    "\n",
    "stations = create_station_nodes(\"./stations.txt\")  # stations.txt 파일로 그래프 노드들을 만든다\n",
    "\n",
    "# stations에 저장한 역들 이름 출력 (체점을 위해 역 이름 순서대로 출력)\n",
    "for station in sorted(stations.keys()):\n",
    "    print(stations[station].station_name)"
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
