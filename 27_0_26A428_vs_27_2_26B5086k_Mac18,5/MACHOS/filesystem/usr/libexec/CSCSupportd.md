## CSCSupportd

> `/usr/libexec/CSCSupportd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-749.0.8.0.0
-  __TEXT.__text: 0x12c14
+749.40.3.0.0
+  __TEXT.__text: 0x12cc0
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0x1ae0
+  __TEXT.__objc_stubs: 0x1b00
   __TEXT.__objc_methlist: 0x534
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x316b
-  __TEXT.__objc_methname: 0x13c8
-  __TEXT.__oslogstring: 0x7fa
+  __TEXT.__cstring: 0x3181
+  __TEXT.__objc_methname: 0x13de
+  __TEXT.__oslogstring: 0x838
   __TEXT.__objc_classname: 0x3c
   __TEXT.__objc_methtype: 0x1f2
   __TEXT.__dlopen_cstrs: 0x50

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__auth_got: 0x448
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__got: 0x168
   __DATA.__objc_const: 0x368
-  __DATA.__objc_selrefs: 0x6e0
+  __DATA.__objc_selrefs: 0x6e8
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x140
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/ServiceManagement.framework/Versions/A/ServiceManagement
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
+  - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/Versions/A/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/Versions/A/RemoteXPC
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 185
-  Symbols:   190
-  CStrings:  762
+  Symbols:   191
+  CStrings:  765
 
Symbols:
+ _OBJC_CLASS_$_MIBUClient
Functions:
~ sub_100001b14 -> sub_100001b8c : 1728 -> 1900
CStrings:
+ "%{public}s: MIBUClient isInPalletUpdateMode error: %{public}@"
+ "_isInPalletUpdateMode"
+ "isInPalletUpdateMode:"
```
