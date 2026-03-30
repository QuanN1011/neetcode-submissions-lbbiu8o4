
// class ListNode:
//     def __init__(self, key = -1, value = -1, next = None):
//         self.key = key
//         self.value = value
//         self.next = next
// class MyHashMap:

//     def __init__(self):
//         self.hashMap = [ListNode() for i in range(1000)]

//     def hashFunction(self, key: int):
//         return key % len(self.hashMap)

//     def put(self, key: int, value: int) -> None:
//         index = self.hashFunction(key)
//         cur = self.hashMap[index]

//         while cur.next:
//             if cur.next.key == key:
//                 cur.next.value = value
//                 return
//             cur = cur.next
        
//         cur.next = ListNode(key, value)

//     def get(self, key: int) -> int:
//         index = self.hashFunction(key)
//         cur = self.hashMap[index].next

//         while cur:
//             if cur.key == key:
//                 return cur.value
//             cur = cur.next

//         return -1

//     def remove(self, key: int) -> None:
//         index = self.hashFunction(key)
//         cur = self.hashMap[index]

//         while cur and cur.next:
//             if cur.next.key == key:
//                 cur.next = cur.next.next
//                 return
//             cur = cur.next

        


// # Your MyHashMap object will be instantiated and called as such:
// # obj = MyHashMap()
// # obj.put(key,value)
// # param_2 = obj.get(key)
// # obj.remove(key)
class MyHashMap {

    private class ListNode{
        int key;
        int value;
        ListNode next;
        
        ListNode(int key, int value){
            this.key = key;
            this.value = value;
            this.next = null;
        }

        ListNode(){
            this.key = -1;
            this.value = -1;
            this.next = null;
        }
    }

    private ListNode[] hashMap;
    private final int SIZE = 1000;

    public MyHashMap() {
        hashMap = new ListNode[SIZE];
        // initialize each index
        for(int i = 0; i < SIZE; i++){
            hashMap[i] = new ListNode();
        }
    }

    public int hashFunction(int key){
        return key % SIZE;
    }
    
    public void put(int key, int value) {
        int index = hashFunction(key);
        ListNode cur = hashMap[index];

        while(cur.next != null){
            if(cur.next.key == key){
                cur.next.value = value;
                return;
            }
            cur = cur.next;
        }
        cur.next = new ListNode(key, value);
        
    }
    
    public int get(int key) {
        int index = hashFunction(key);
        ListNode cur = hashMap[index];

        while(cur != null){
            if(cur.key == key){
                return cur.value;
            }
            cur = cur.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        int index = hashFunction(key);
        ListNode cur = hashMap[index];

        while(cur != null && cur.next != null){
            if(cur.next.key == key){
                cur.next = cur.next.next;
                return;
            }
            cur = cur.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */