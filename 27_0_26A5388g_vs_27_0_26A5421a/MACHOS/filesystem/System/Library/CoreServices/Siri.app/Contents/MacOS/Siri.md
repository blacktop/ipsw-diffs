## Siri

> `/System/Library/CoreServices/Siri.app/Contents/MacOS/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3600.46.14.0.0
-  __TEXT.__text: 0x29044
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_stubs: 0x5f60
-  __TEXT.__objc_methlist: 0x26d8
+3600.46.19.14.4
+  __TEXT.__text: 0x293e0
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_stubs: 0x5fa0
+  __TEXT.__objc_methlist: 0x26e8
   __TEXT.__const: 0x414
   __TEXT.__objc_classname: 0x5b3
-  __TEXT.__objc_methname: 0x8356
+  __TEXT.__objc_methname: 0x83a6
   __TEXT.__objc_methtype: 0x1cd1
-  __TEXT.__cstring: 0x4414
+  __TEXT.__cstring: 0x4404
   __TEXT.__gcc_except_tab: 0x4e0
-  __TEXT.__oslogstring: 0x3248
+  __TEXT.__oslogstring: 0x33f8
   __TEXT.__swift5_typeref: 0x20a
   __TEXT.__swift5_capture: 0x178
   __TEXT.__constg_swiftt: 0x278

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0xac0
+  __TEXT.__unwind_info: 0xac8
   __TEXT.__eh_frame: 0x2d8
   __DATA_CONST.__const: 0x1280
-  __DATA_CONST.__cfstring: 0x1480
+  __DATA_CONST.__cfstring: 0x14a0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0x6e8
+  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__got: 0x6f0
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA.__objc_const: 0x50e0
-  __DATA.__objc_selrefs: 0x2060
-  __DATA.__objc_ivar: 0x1dc
+  __DATA.__objc_const: 0x5100
+  __DATA.__objc_selrefs: 0x2070
+  __DATA.__objc_ivar: 0x1e0
   __DATA.__objc_data: 0x7c8
   __DATA.__data: 0xd48
   __DATA.__bss: 0x2c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1015
-  Symbols:   539
-  CStrings:  2192
+  Functions: 1019
+  Symbols:   541
+  CStrings:  2199
 
Symbols:
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSStatusItem
CStrings:
+ "%s [Campo] Status menu long press released after threshold. Consumed event."
+ "%s [Invocation] Accepting connection %@ entitled:%d"
+ "%s [Invocation] Long press released after threshold. Consumed event."
+ "%s [Invocation] Process %@ is attempting to submit text to Siri without entitlement."
+ "%s [Invocation] Received Notification with identifier '%@' from pid %d"
+ "%s [Invocation] SiriNCActionPrewarm reached handleAction: — it should be filtered out in -[SiriNCService invokeService:...] and never arrive here. Listed for switch exhaustiveness."
+ "_ncServiceConnectionToken"
+ "_statusItemUsesDirectEvents"
+ "instancesRespondToSelector:"
+ "setNeedsDirectEvents:"
+ "\xf0\xc1"
- "%s [Invocation] Invoking Siri with entitlement."
- "%s [Invocation] Received Notification with identifier '%@'"
- "-[SiriUXAppDelegate connectToNCService]"
- "\xf0\xb1"
```
