## SAMaintenance

> `/System/Library/ExtensionKit/Extensions/SAMaintenance.appex/Contents/MacOS/SAMaintenance`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`

```diff

-3600.85.1.0.0
-  __TEXT.__text: 0x15f0
-  __TEXT.__auth_stubs: 0x360
+3605.33.1.0.0
+  __TEXT.__text: 0x15ec
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__const: 0x122
-  __TEXT.__cstring: 0x28
+  __TEXT.__cstring: 0x35
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x23
   __TEXT.__constg_swiftt: 0x50

   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x90
-  __DATA.__data: 0xd8
+  __DATA.__data: 0xc8
   __DATA.__common: 0x18
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 33
-  Symbols:   55
-  CStrings:  6
+  Symbols:   54
+  CStrings:  7
 
Symbols:
- _swift_bridgeObjectRetain
Functions:
~ sub_100001288 : 132 -> 128
CStrings:
+ "SAMaintenance.Plugin"
+ "com.apple.siri.analytics"
- "com.apple.siri.analytics.SAMaintenance"
```
