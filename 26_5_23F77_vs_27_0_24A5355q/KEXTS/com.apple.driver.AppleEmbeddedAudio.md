## com.apple.driver.AppleEmbeddedAudio

> `com.apple.driver.AppleEmbeddedAudio`

```diff

-940.17.0.0.0
-  __TEXT.__cstring: 0x4319
+1000.40.0.0.0
+  __TEXT.__cstring: 0x44f8
   __TEXT.__const: 0xb0
   __TEXT.__os_log: 0x32b4
-  __TEXT_EXEC.__text: 0x351b0
+  __TEXT_EXEC.__text: 0x35248
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x308
   __DATA.__common: 0x458
-  __DATA_CONST.__auth_got: 0x508
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x78
   __DATA_CONST.__mod_term_func: 0x78
-  __DATA_CONST.__const: 0xd048
+  __DATA_CONST.__const: 0xd0d0
   __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: AFD9ADFB-24E1-376F-A736-8D46C083951E
-  Functions: 1116
+  __DATA_CONST.__auth_got: 0x508
+  __DATA_CONST.__got: 0x110
+  UUID: DBFD1E1C-D200-3D9F-8CA8-534DD4DC8072
+  Functions: 1121
   Symbols:   0
-  CStrings:  714
+  CStrings:  720
 
CStrings:
+ "\"%s\" @%s:%d"
+ "OSBoundedPtr.h"
+ "The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range"
+ "This bounded_ptr is pointing to memory outside of what can be represented by a native pointer."
+ "bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally"
+ "bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow."

```
