## spindump

> `/usr/sbin/spindump`

```diff

-410.0.0.0.0
-  __TEXT.__text: 0xbd1e8
+411.0.0.0.0
+  __TEXT.__text: 0xbe1b4
   __TEXT.__auth_stubs: 0x12d0
   __TEXT.__objc_stubs: 0x40a0
   __TEXT.__objc_methlist: 0x9f4
   __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x140c7
-  __TEXT.__oslogstring: 0x24b16
+  __TEXT.__cstring: 0x142ef
+  __TEXT.__oslogstring: 0x24df0
   __TEXT.__objc_classname: 0x105
   __TEXT.__gcc_except_tab: 0x32f4
   __TEXT.__objc_methname: 0x41b5
   __TEXT.__objc_methtype: 0x530
-  __TEXT.__unwind_info: 0xdd8
+  __TEXT.__unwind_info: 0xde0
   __DATA_CONST.__auth_got: 0x978
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x14b0
-  __DATA_CONST.__cfstring: 0x9720
+  __DATA_CONST.__cfstring: 0x9840
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 71AEE9BC-FEBF-3F4C-9973-FAAC74C30DF2
-  Functions: 1738
+  UUID: F890CBBA-93AB-3B40-8053-BF1253253F15
+  Functions: 1744
   Symbols:   379
-  CStrings:  4558
+  CStrings:  4582
 
CStrings:
+ "\nswift-inspect dump-concurrency output for %s [%d]\nswift-inspect dump-concurrency %d\n"
+ "%s [%d]: No output from swift-inspect dump-concurrency for %d"
+ "%s [%d]: Unable to spawn swift-inspect: %d (%s)"
+ "%{public}s [%d]: No output from swift-inspect dump-concurrency for %d"
+ "%{public}s [%d]: Unable to spawn swift-inspect: %d (%s)"
+ "/usr/bin/swift-inspect"
+ "No output from swift-inspect dump-concurrency for %d"
+ "No output from swift-inspect dump-concurrency for %d\n"
+ "Running swift-inspect dump-concurrency for %s [%d]"
+ "Unable to format: %s [%d]: No output from swift-inspect dump-concurrency for %d"
+ "Unable to format: %s [%d]: Unable to spawn swift-inspect: %d (%s)"
+ "Unable to format: No output from swift-inspect dump-concurrency for %d"
+ "Unable to format: Running swift-inspect dump-concurrency for %s [%d]"
+ "Unable to format: Unable to spawn swift-inspect: %d (%s)"
+ "Unable to format: swift-inspect dump-concurrency for [%d] completed"
+ "Unable to spawn swift-inspect for %d: %d %s\n"
+ "Unable to spawn swift-inspect: %d (%s)"
+ "com.apple.swift-inspect"
+ "dump-concurrency"
+ "swift-inspect dump-concurrency for [%d] completed"

```
