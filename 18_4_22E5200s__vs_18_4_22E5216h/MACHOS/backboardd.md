## backboardd

> `/usr/libexec/backboardd`

```diff

-668.5.24.0.0
-  __TEXT.__text: 0xa332c
-  __TEXT.__auth_stubs: 0x1ca0
+668.5.27.1.0
+  __TEXT.__text: 0xa37ac
+  __TEXT.__auth_stubs: 0x1cb0
   __TEXT.__objc_stubs: 0xeb20
-  __TEXT.__objc_methlist: 0x73b4
+  __TEXT.__objc_methlist: 0x73cc
   __TEXT.__const: 0x4e0
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__gcc_except_tab: 0x5168
-  __TEXT.__objc_methname: 0x14d82
-  __TEXT.__cstring: 0x74f0
-  __TEXT.__objc_classname: 0x1c0a
+  __TEXT.__gcc_except_tab: 0x5178
+  __TEXT.__objc_methname: 0x14e32
+  __TEXT.__cstring: 0x7573
+  __TEXT.__objc_classname: 0x1c0c
   __TEXT.__objc_methtype: 0x4009
-  __TEXT.__oslogstring: 0xa333
+  __TEXT.__oslogstring: 0xa39a
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x29e8
-  __DATA_CONST.__auth_got: 0xe68
+  __TEXT.__unwind_info: 0x2a00
+  __DATA_CONST.__auth_got: 0xe70
   __DATA_CONST.__got: 0xa18
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x4ce0
-  __DATA_CONST.__cfstring: 0x8360
+  __DATA_CONST.__cfstring: 0x8440
   __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x238

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x12fd8
+  __DATA.__objc_const: 0x130a0
   __DATA.__objc_selrefs: 0x45f0
-  __DATA.__objc_ivar: 0xf70
+  __DATA.__objc_ivar: 0xf88
   __DATA.__objc_data: 0x3890
   __DATA.__data: 0x1b58
   __DATA.__bss: 0x418

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 3187
-  Symbols:   788
-  CStrings:  6347
+  Functions: 3192
+  Symbols:   789
+  CStrings:  6362
 
Symbols:
+ _BSLogAddStateCaptureBlock
CStrings:
+ "\x12\x1fA\x11#!\x1f\x04\""
+ "C\x11\x11\x11\x13"
+ "Freeze brightness:%{BOOL}u to current value -- %{public}@"
+ "_brightnessCurrentlyFrozen"
+ "_displaysBecomingUninterestingByUUID"
+ "_lastBrightnessFreezeReason"
+ "_lastBrightnessFreezeTime"
+ "_lastBrightnessUnfreezeReason"
+ "_lastBrightnessUnfreezeTime"
+ "backlight locked now:%{BOOL}u for render overlays"
+ "brightnessFreeze"
+ "currentlyFrozen"
+ "display %{public}@ became interesting because %{public}@"
+ "display %{public}@ became uninteresting because %{public}@"
+ "dropping uninteresting displays %{public}@"
+ "lastFreezeReason"
+ "lastFreezeTime"
+ "lastUnfreezeReason"
+ "lastUnfreezeTime"
- "\x12\x1eA\x11#!\x1f\x04\""
- "C\x11\x13"
- "Locking backlight to current value: %@ for reason: %{public}@"
- "display %{public}@ interesting because %{public}@"
- "display %{public}@ uninteresting because %{public}@"

```
