## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-  __TEXT.__text: 0x1b338
-  __TEXT.__auth_stubs: 0x1520
-  __TEXT.__objc_stubs: 0x880
+  __TEXT.__text: 0x1b77c
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_stubs: 0x920
   __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__cstring: 0xaa47
-  __TEXT.__const: 0x6e8
+  __TEXT.__cstring: 0xacf5
+  __TEXT.__const: 0x6f8
   __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__objc_methname: 0x7c6
+  __TEXT.__objc_methname: 0x809
   __TEXT.__objc_classname: 0x5b
   __TEXT.__objc_methtype: 0x159
-  __TEXT.__unwind_info: 0x400
+  __TEXT.__unwind_info: 0x408
   __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x20a0
+  __DATA_CONST.__cfstring: 0x20e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0xaa8
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_got: 0xab8
+  __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x400
-  __DATA.__objc_selrefs: 0x2e0
+  __DATA.__objc_selrefs: 0x308
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x250

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 273
-  Symbols:   398
-  CStrings:  1645
+  Functions: 276
+  Symbols:   402
+  CStrings:  1667
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _IOMobileFramebufferSetBrightnessControlCallback
+ _IOServiceWaitQuiet
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_NSDate
CStrings:
+ "%s: %s: IOMobileFramebufferCreateDisplayList failed"
+ "%s: %s: IOMobileFramebufferOpenByName failed: 0x%x"
+ "%s: %s: IOMobileFramebufferSetBrightnessControlCallback failed: 0x%x"
+ "%s: %s: IOMobileFramebufferSwapBegin failed: 0x%x"
+ "%s: %s: IOMobileFramebufferSwapEnd failed: 0x%x"
+ "%s: %s: IOMobileFramebufferSwapSetBrightness failed: 0x%x"
+ "%s: %s: IOMobileFramebufferSwapWaitWithTimeout failed: 0x%x"
+ "%s: %s: NVMe sanitize failed on %s"
+ "%s: %s: NVMe sanitize stalled on %s"
+ "%s: %s: Timed out waiting for container to quiesce after Data volume deletion"
+ "%s: %s: no embedded panel found"
+ "%s: %s: timed out waiting for brightness control callback"
+ "Sanitize Status"
+ "broadcast"
+ "dateWithTimeIntervalSinceNow:"
+ "lock"
+ "nvme_sanitize_poll"
+ "turn_on_backlight_iomfb"
+ "unlock"
+ "waitUntilDate:"

```
