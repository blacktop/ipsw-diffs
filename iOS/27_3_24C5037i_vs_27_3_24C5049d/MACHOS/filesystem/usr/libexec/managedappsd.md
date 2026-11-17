## managedappsd

> `/usr/libexec/managedappsd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-113.60.5.0.0
-  __TEXT.__text: 0x12f0
-  __TEXT.__auth_stubs: 0x360
+113.60.10.0.0
+  __TEXT.__text: 0x154c
+  __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_stubs: 0x60
   __TEXT.__const: 0x62
-  __TEXT.__oslogstring: 0x93
+  __TEXT.__oslogstring: 0xb3
   __TEXT.__swift5_typeref: 0x15
   __TEXT.__swift5_entry: 0x8
   __TEXT.__cstring: 0x16

   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__auth_got: 0x1d8
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x18
   __DATA.__data: 0x18
-  __DATA.__common: 0x60
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 16
-  Symbols:   76
-  CStrings:  9
+  Functions: 17
+  Symbols:   80
+  CStrings:  10
 
Symbols:
+ _$s15ManagedAppsCore0aB26SiriAIExclusionsControllerC5scopeAC0aB9Interface0aB12ServiceScopeO_tcfC
+ _$s15ManagedAppsCore0aB26SiriAIExclusionsControllerC5startyyF
+ _$s15ManagedAppsCore0aB26SiriAIExclusionsControllerCMa
+ _objc_release_x23
CStrings:
+ "%s setup: device configuration"
```
