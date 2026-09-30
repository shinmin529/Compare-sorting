# experiment.py
import time
import random
from sorting_algorithms import insertion_sort, merge_sort, heap_sort

def run_experiments():
    sizes = [1000, 5000, 10000, 50000]
    
    print("=== 고급 알고리즘 과제 1: 정렬 알고리즘 성능 측정 ===")
    
    for n in sizes:
        print(f"\n--- 입력 크기 n = {n} ---")
        
        # 데이터 세트 생성
        random_data = [random.randint(1, 100000) for _ in range(n)]
        sorted_data = sorted(random_data)
        reversed_data = list(reversed(sorted_data))
        duplicate_data = [random.randint(1, 10) for _ in range(n)] # 중복 많음
        
        datasets = {
            "Random": random_data,
            "Sorted": sorted_data,
            "Reversed": reversed_data,
            "Duplicates": duplicate_data
        }
        
        for name, data in datasets.items():
            # 1. 병합 정렬 측정
            arr_m = data.copy()
            start = time.perf_counter()
            merge_sort(arr_m)
            end = time.perf_counter()
            merge_time = end - start
            
            # 2. 힙 정렬 측정
            arr_h = data.copy()
            start = time.perf_counter()
            heap_sort(arr_h)
            end = time.perf_counter()
            heap_time = end - start
            
            # 3. 삽입 정렬 측정 (크기가 너무 크면 느리므로 대상을 제한하거나 그대로 측정)
            arr_i = data.copy()
            start = time.perf_counter()
            insertion_sort(arr_i)
            end = time.perf_counter()
            insertion_time = end - start
            
            print(f"[{name}] Insertion: {insertion_time:.5f}s | Merge: {merge_time:.5f}s | Heap: {heap_time:.5f}s")

if __name__ == "__main__":
    run_experiments()