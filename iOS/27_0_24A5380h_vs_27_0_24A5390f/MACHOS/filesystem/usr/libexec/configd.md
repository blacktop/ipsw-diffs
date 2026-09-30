## configd

> `/usr/libexec/configd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1441.0.0.0.0
-  __TEXT.__text: 0x68ab0
-  __TEXT.__auth_stubs: 0x24e0
+1444.0.0.0.0
+  __TEXT.__text: 0x68fac
+  __TEXT.__auth_stubs: 0x24d0
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__objc_methlist: 0xa64
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x3026
-  __TEXT.__oslogstring: 0x564d
+  __TEXT.__cstring: 0x3044
+  __TEXT.__oslogstring: 0x56dd
   __TEXT.__objc_methname: 0x1a6b
   __TEXT.__objc_classname: 0x54
   __TEXT.__objc_methtype: 0x501
   __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__unwind_info: 0xa28
-  __DATA_CONST.__const: 0x19d0
-  __DATA_CONST.__cfstring: 0x25c0
+  __TEXT.__unwind_info: 0xa50
+  __DATA_CONST.__const: 0x19f0
+  __DATA_CONST.__cfstring: 0x2580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__auth_got: 0x1280
+  __DATA_CONST.__auth_got: 0x1278
   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x110
   __DATA.__objc_const: 0xc48

   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x104
-  __DATA.__common: 0x80
+  __DATA.__common: 0x88
   __DATA.__bss: 0x640
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 955
-  Symbols:   819
-  CStrings:  1668
+  Functions: 962
+  Symbols:   818
+  CStrings:  1673
 
Symbols:
- _CFArrayGetValues
CStrings:
+ "  %d : port = 0x%x (%u)"
+ "%s: all done waiting"
+ "%s: delaying shutdown by %d seconds"
+ "/var/tmp/configd-watcher.plist"
+ "configd: bundle shutdown complete"
+ "configd: calling stop() on %@"
+ "configd: handling SIGTERM"
+ "configd: no plugins need stop, exiting"
+ "configd: stopping plugins"
+ "no plugins delayed stop"
+ "stop_IPMonitor"
- "  %d : port = 0x%x"
- "calling bundle stop() functions"
- "server shutdown complete (%f)"
- "starting server shutdown (%f)"
- "watcherRefs"
- "watchers"
```
