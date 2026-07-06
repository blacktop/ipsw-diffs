## com.apple.driver.AppleT8150MCC

> `com.apple.driver.AppleT8150MCC`

```diff

   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x5ba7
   __TEXT.__os_log: 0x2701
-  __TEXT_EXEC.__text: 0x169b4
+  __TEXT_EXEC.__text: 0x169a8
   __TEXT_EXEC.__auth_stubs: 0x5b0
   __DATA.__data: 0x9130
   __DATA.__common: 0x1f0

   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xc0
-  Functions: 570
+  Functions: 569
   Symbols:   0
   CStrings:  934
 
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ __ZN25AppleMemCacheControllerV29getPTDIdxEPKcPjS2_ : 620 -> 624
~ __ZN11MemCacheCIP5startEP9IOService : 4768 -> 4804
- __ZN11MemCacheCIP5startEP9IOService.cold.10
CStrings:
+ "\"%s: \" \"Total AMCC Count %d exceeds the max value that the _amccEnableMask can represent\" @%s:%d"
- "\"%s: \" \"Total AMCC Count %d exceeds the max value that the _amccEnbaleMask can represent\" @%s:%d"

```
