## SiriLogProcessor

> `/System/Library/ExtensionKit/Extensions/SiriLogProcessor.appex/SiriLogProcessor`

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
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-2.9.0.0.0
-  __TEXT.__text: 0x16d4
+3.3.0.0.0
+  __TEXT.__text: 0x16dc
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__const: 0x1da
-  __TEXT.__cstring: 0x27
+  __TEXT.__cstring: 0x39
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x29
   __TEXT.__objc_methname: 0x1e

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 41
   Symbols:   49
-  CStrings:  5
+  CStrings:  6
 
Functions:
~ sub_100001380 : 132 -> 140
CStrings:
+ "Siri.LogProcessor.Plugin"
+ "com.apple.unilog.processing"
- "com.apple.unilog.siri.SiriLogProcessor"
```
