import java.util.HashMap;
import java.util.Map;

class LRUCache {

    HashMap<Integer, Integer> cache = new HashMap<>();
    final int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {

        return -1;
    }

    public void put(int key, int value) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */