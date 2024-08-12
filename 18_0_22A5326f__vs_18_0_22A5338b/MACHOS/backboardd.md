## backboardd

> `/usr/libexec/backboardd`

```diff

-668.1.3.0.0
-  __TEXT.__text: 0x9ed44
-  __TEXT.__auth_stubs: 0x1c40
-  __TEXT.__objc_stubs: 0xe960
-  __TEXT.__objc_methlist: 0x6754
+668.1.5.0.0
+  __TEXT.__text: 0x9f900
+  __TEXT.__auth_stubs: 0x1c50
+  __TEXT.__objc_stubs: 0xe9a0
+  __TEXT.__objc_methlist: 0x6774
   __TEXT.__const: 0x518
   __TEXT.__gcc_except_tab: 0x4f54
-  __TEXT.__objc_methname: 0x149b5
-  __TEXT.__cstring: 0x706d
+  __TEXT.__objc_methname: 0x14a54
+  __TEXT.__cstring: 0x711e
   __TEXT.__objc_classname: 0x1c70
   __TEXT.__objc_methtype: 0x3fed
-  __TEXT.__oslogstring: 0x9d0c
+  __TEXT.__oslogstring: 0x9e5c
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x2960
-  __DATA_CONST.__auth_got: 0xe38
+  __TEXT.__unwind_info: 0x2980
+  __DATA_CONST.__auth_got: 0xe40
   __DATA_CONST.__got: 0xa18
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4a88
-  __DATA_CONST.__cfstring: 0x7ca0
+  __DATA_CONST.__const: 0x4ad8
+  __DATA_CONST.__cfstring: 0x7ce0
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x240

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x14038
-  __DATA.__objc_selrefs: 0x44d8
-  __DATA.__objc_ivar: 0xf18
+  __DATA.__objc_const: 0x14058
+  __DATA.__objc_selrefs: 0x44f8
+  __DATA.__objc_ivar: 0xf1c
   __DATA.__objc_data: 0x3930
   __DATA.__data: 0x1bb0
   __DATA.__bss: 0x418

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 3112
-  Symbols:   783
-  CStrings:  6218
+  Functions: 3119
+  Symbols:   784
+  CStrings:  6239
 
Symbols:
+ _CFRunLoopWakeUp
CStrings:
+ "\x12\x13\x11"
+ "%!@(MISSING) BKDisplayLink:%!p(MISSING) for %!@(MISSING)"
+ "BKDisplayGetSystemIdentifiers"
+ "BKDisplayLink %!p(MISSING) _thread_invalidate"
+ "BKDisplayLink %!p(MISSING) _thread_invalidate already invalid"
+ "BKDisplayLink %!p(MISSING) invalidate finish"
+ "BKDisplayLink %!p(MISSING) invalidate start "
+ "BKDisplayLink init %!p(MISSING) %!{(MISSING)public}@"
+ "BKDisplayLink.m"
+ "BKDisplaySetSystemIdentifiers"
+ "Error unarchiving system identifiers"
+ "GetSystemIdentifiers failed to encode system identifiers"
+ "GetSystemIdentifiers: no active system identifiers"
+ "_BKDisplayXXGetSystemIdentifiers"
+ "_BKDisplayXXSetSystemIdentifiers"
+ "_paused"
+ "_thread_displayLink"
+ "_thread_invalid"
+ "_thread_invalidate"
+ "_thread_setPaused:"
+ "must -invalidate before dealloc"
+ "performSelector:onThread:withObject:waitUntilDone:"
+ "setSystemIdentifiers:"
+ "systemIdentifiers"
- "\x13\x12\x11"
- "%!@(MISSING) BKDisplayLink for %!@(MISSING)"
- "performBlock:"

```
