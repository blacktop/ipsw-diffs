## com.apple.tailspin

> `/System/Library/UserEventPlugins/com.apple.tailspin.plugin/com.apple.tailspin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA.__const`

```diff

-268.0.0.0.0
-  __TEXT.__text: 0x610
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0xa0
+268.1.0.0.0
+  __TEXT.__text: 0x728
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0x140
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x8c
+  __TEXT.__cstring: 0xbb
   __TEXT.__oslogstring: 0x11c
-  __TEXT.__objc_methname: 0x5a
+  __TEXT.__objc_methname: 0xb3
   __TEXT.__unwind_info: 0x80
   __DATA.__const: 0x48
-  __DATA.__cfstring: 0x40
+  __DATA.__cfstring: 0xc0
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x28
+  __DATA.__objc_selrefs: 0x50
   __DATA.__crash_info: 0x148
-  __DATA.__auth_got: 0x120
-  __DATA.__got: 0x18
+  __DATA.__auth_got: 0x140
+  __DATA.__got: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 7
-  Symbols:   46
-  CStrings:  20
+  Symbols:   52
+  CStrings:  29
 
Symbols:
+ _CFPreferencesCopyKeyList
+ _OBJC_CLASS_$_NSMutableArray
+ _kCFPreferencesAnyHost
+ _objc_alloc_init
+ _objc_enumerationMutation
+ _objc_retain
Functions:
~ _init_tailspin : 1168 -> 1448
CStrings:
+ "%@."
+ "HTThirdPartyDevSupport"
+ "addObject:"
+ "com.apple.da"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "hasPrefix:"
+ "mobile"
+ "stringWithFormat:"
```
