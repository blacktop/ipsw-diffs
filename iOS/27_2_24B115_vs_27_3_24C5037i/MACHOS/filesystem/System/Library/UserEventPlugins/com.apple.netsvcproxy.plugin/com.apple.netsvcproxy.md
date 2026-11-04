## com.apple.netsvcproxy

> `/System/Library/UserEventPlugins/com.apple.netsvcproxy.plugin/com.apple.netsvcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA.__const`
- `__DATA.__cfstring`
- `__DATA.__objc_classlist`
- `__DATA.__objc_protolist`
- `__DATA.__objc_const`
- `__DATA.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__objc_arrayobj`
- `__DATA.__got`

```diff

-990.40.2.0.0
-  __TEXT.__text: 0x9fc4
-  __TEXT.__auth_stubs: 0x820
+990.60.10.0.1
+  __TEXT.__text: 0xa280
+  __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0x1cc0
-  __TEXT.__objc_methlist: 0xb00
-  __TEXT.__objc_methname: 0x2a36
+  __TEXT.__objc_methlist: 0xb10
+  __TEXT.__objc_methname: 0x2a6a
   __TEXT.__cstring: 0xfa7
   __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methtype: 0x300
+  __TEXT.__objc_methtype: 0x30e
   __TEXT.__const: 0x2a0
   __TEXT.__gcc_except_tab: 0x268
   __TEXT.__oslogstring: 0xb72

   __DATA.__objc_protolist: 0x10
   __DATA.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x1008
-  __DATA.__objc_selrefs: 0x998
+  __DATA.__objc_selrefs: 0x9a0
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x140
   __DATA.__data: 0xd4
   __DATA.__objc_arraydata: 0x18
   __DATA.__objc_arrayobj: 0x18
-  __DATA.__auth_got: 0x420
+  __DATA.__auth_got: 0x428
   __DATA.__got: 0x1d8
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 315
-  Symbols:   217
-  CStrings:  769
+  Functions: 316
+  Symbols:   218
+  CStrings:  771
 
Symbols:
+ _dispatch_queue_attr_make_with_autorelease_frequency
CStrings:
+ "Q32@0:8@16@24"
+ "copyAllItemsFromKeychainWithIdentifier:"
+ "totalDataInKeychainWithIdentifier:accountName:"
- "totalDataInKeychainWithIdentifier:"
```
