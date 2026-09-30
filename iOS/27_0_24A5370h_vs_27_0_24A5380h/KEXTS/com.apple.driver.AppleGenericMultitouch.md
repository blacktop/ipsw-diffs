## com.apple.driver.AppleGenericMultitouch

> `com.apple.driver.AppleGenericMultitouch`

```diff

-  __TEXT.__cstring: 0x6ccc
+  __TEXT.__cstring: 0x6d1b
   __TEXT.__const: 0x236
-  __TEXT.__os_log: 0x2ae7
-  __TEXT_EXEC.__text: 0xa390
-  __TEXT_EXEC.__auth_stubs: 0x370
+  __TEXT.__os_log: 0x2b8c
+  __TEXT_EXEC.__text: 0xa61c
+  __TEXT_EXEC.__auth_stubs: 0x380
   __DATA.__data: 0xd4
   __DATA.__common: 0xa8
   __DATA.__bss: 0x1

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1780
   __DATA_CONST.__kalloc_type: 0x200
-  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0xc8
-  Functions: 244
+  Functions: 247
   Symbols:   0
-  CStrings:  323
+  CStrings:  326
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
CStrings:
+ "12111112122212121111112"
+ "IOReturn AppleGenericMultitouchDecider::helperStateChangedGated(AppleGenericMultitouchDeciderHelper *)"
+ "[Decider] Already launched, ignoring state change\n%s line %d"
+ "_commandGate"
+ "getWorkLoop()->addEventSource(_commandGate.get()) == 0"
- "121111121222121211111"
- "void AppleGenericMultitouchDecider::helperStateChanged(AppleGenericMultitouchDeciderHelper *)"

```
