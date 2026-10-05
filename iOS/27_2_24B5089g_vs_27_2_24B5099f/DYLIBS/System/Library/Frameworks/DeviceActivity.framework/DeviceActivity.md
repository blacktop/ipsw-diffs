## DeviceActivity

> `/System/Library/Frameworks/DeviceActivity.framework/DeviceActivity`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-407.1.4.0.0
-  __TEXT.__text: 0x92ed8
+407.1.5.0.0
+  __TEXT.__text: 0x9297c
   __TEXT.__objc_methlist: 0x4b0
   __TEXT.__const: 0x3c38
   __TEXT.__constg_swiftt: 0xe98

   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x50
   __TEXT.__swift_as_cont: 0x98
-  __TEXT.__unwind_info: 0x2270
-  __TEXT.__eh_frame: 0x2ef8
+  __TEXT.__unwind_info: 0x2288
+  __TEXT.__eh_frame: 0x2f28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__const: 0x32c0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0xd20
-  __AUTH_CONST.__auth_got: 0xcf8
+  __AUTH_CONST.__auth_got: 0xd08
   __AUTH.__objc_data: 0x120
   __AUTH.__data: 0x600
-  __DATA.__data: 0x968
-  __DATA.__common: 0x60
+  __DATA.__data: 0x950
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__data: 0x10e8
-  __DATA_DIRTY.__bss: 0x1480
-  __DATA_DIRTY.__common: 0xa0
+  __DATA_DIRTY.__data: 0x1118
+  __DATA_DIRTY.__bss: 0x1500
+  __DATA_DIRTY.__common: 0xd0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2506
-  Symbols:   802
+  Functions: 2508
+  Symbols:   803
   CStrings:  182
 
Symbols:
+ _swift_retain_x8
CStrings:
+ "Refreshing all activity due to queryStart (%{public}s) being after now (%{public}s)"
- "Skipping refresh because query start: %{public}s, is out of bounds: %{public}s - %{public}s"
```
