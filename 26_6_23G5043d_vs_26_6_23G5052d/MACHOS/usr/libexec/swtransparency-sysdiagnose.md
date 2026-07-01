## swtransparency-sysdiagnose

> `/usr/libexec/swtransparency-sysdiagnose`

```diff

   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x118
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0xd0

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 72
-  Symbols:   129
+  Symbols:   130
   CStrings:  7
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ __swift_FORCE_LOAD_$_swiftOSLog

```
