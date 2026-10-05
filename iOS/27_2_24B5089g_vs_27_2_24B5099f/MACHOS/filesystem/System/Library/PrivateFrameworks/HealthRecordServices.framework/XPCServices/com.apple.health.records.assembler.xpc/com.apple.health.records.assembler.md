## com.apple.health.records.assembler

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/XPCServices/com.apple.health.records.assembler.xpc/com.apple.health.records.assembler`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0x101c
-  __TEXT.__auth_stubs: 0x330
+7027.1.54.2.3
+  __TEXT.__text: 0x1038
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_stubs: 0x20
   __TEXT.__const: 0x22
   __TEXT.__swift5_entry: 0x8
   __TEXT.__oslogstring: 0x19
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0xc
+  __TEXT.__objc_methname: 0x5
   __TEXT.__unwind_info: 0xd0
   __TEXT.__eh_frame: 0xd0
   __DATA_CONST.__const: 0xc9
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x198
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x70
+  __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x20
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices
   - /System/Library/PrivateFrameworks/HealthRecordsAssembler.framework/HealthRecordsAssembler
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 22
-  Symbols:   54
-  CStrings:  1
+  Symbols:   57
+  CStrings:  2
 
Symbols:
+ _OBJC_CLASS_$_HKHealthStore
+ _objc_allocWithZone
+ _objc_msgSend
Functions:
~ sub_100001060 -> sub_1000011a8 : 832 -> 860
CStrings:
+ "init"
```
