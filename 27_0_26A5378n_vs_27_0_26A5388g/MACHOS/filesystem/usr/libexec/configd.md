## configd

> `/usr/libexec/configd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1441.0.0.0.0
-  __TEXT.__text: 0x6c994
-  __TEXT.__auth_stubs: 0x2460
+1444.0.0.0.0
+  __TEXT.__text: 0x6cb48
+  __TEXT.__auth_stubs: 0x2450
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0xb64
   __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x3252
-  __TEXT.__oslogstring: 0x5993
+  __TEXT.__cstring: 0x3261
+  __TEXT.__oslogstring: 0x59ea
   __TEXT.__objc_methname: 0x1c8d
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x672
   __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__unwind_info: 0xa80
+  __TEXT.__unwind_info: 0xa98
   __DATA_CONST.__const: 0x19c8
-  __DATA_CONST.__cfstring: 0x2a20
+  __DATA_CONST.__cfstring: 0x29e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__auth_got: 0x1240
+  __DATA_CONST.__auth_got: 0x1238
   __DATA_CONST.__got: 0x710
   __DATA_CONST.__auth_ptr: 0x108
   __DATA.__objc_const: 0xde8

   __DATA.__objc_ivar: 0xa0
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x168
-  __DATA.__common: 0x80
+  __DATA.__common: 0x88
   __DATA.__bss: 0x698
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 994
-  Symbols:   820
-  CStrings:  1773
+  Functions: 999
+  Symbols:   819
+  CStrings:  1775
 
Symbols:
- _CFArrayGetValues
CStrings:
+ "  %d : port = 0x%x (%u)"
+ "/var/tmp/configd-watcher.plist"
+ "configd: bundle shutdown complete"
+ "configd: calling stop() on %@"
+ "configd: handling SIGTERM"
+ "configd: no plugins need stop, exiting"
+ "configd: stopping plugins"
+ "no plugins delayed stop"
- "  %d : port = 0x%x"
- "calling bundle stop() functions"
- "server shutdown complete (%f)"
- "starting server shutdown (%f)"
- "watcherRefs"
- "watchers"
```
