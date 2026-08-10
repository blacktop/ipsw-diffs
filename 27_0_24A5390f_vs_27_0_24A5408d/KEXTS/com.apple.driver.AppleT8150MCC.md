## com.apple.driver.AppleT8150MCC

> `com.apple.driver.AppleT8150MCC`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-127.0.1.0.0
+127.0.3.0.0
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x5ba7
-  __TEXT.__os_log: 0x2701
-  __TEXT_EXEC.__text: 0x169a8
+  __TEXT.__cstring: 0x5d0f
+  __TEXT.__os_log: 0x26ff
+  __TEXT_EXEC.__text: 0x16af0
   __TEXT_EXEC.__auth_stubs: 0x5b0
   __DATA.__data: 0x9130
   __DATA.__common: 0x1f0

   __DATA_CONST.__got: 0xc0
   Functions: 569
   Symbols:   0
-  CStrings:  934
+  CStrings:  939
 
Functions:
~ __ZN11MemCacheCIP5startEP9IOService : 4804 -> 5132
CStrings:
+ "\"%s: \" \"Per-die DCS channel count %u exceeds 32 bits\" @%s:%d"
+ "\"%s: \" \"Per-die dcs-channel-enable-mask 0x%llx has bits beyond dcsPerDie=%u\" @%s:%d"
+ "\"%s: \" \"Total DCS channel count %u exceeds width of _dcsChannelEnableMask\" @%s:%d"
+ "\"%s: \" \"dcs-count-per-amcc %u * amccsPerDie %u overflows uint32_t\" @%s:%d"
+ "\"%s: \" \"dcsPerDie %u * _dieNum %u overflows uint32_t\" @%s:%d"
+ "%s:%d: dcs-channel-enable-mask (per-die from EDT): 0x%llx\n\n"
+ "%s:%d: dcs-channel-enable-mask not in EDT; defaulting to 0x%llx\n"
+ "dcs-channel-enable-mask (per-die from EDT): 0x%llx\n"
+ "dcs-channel-enable-mask not in EDT; defaulting to 0x%llx"
- "%s:%d: dcs-channel-enable-mask is not set in EDT. Setting dcs channel mask to 0x%llx\n"
- "%s:%d: dcs-channel-enable-mask: 0x%llx\n\n"
- "dcs-channel-enable-mask is not set in EDT. Setting dcs channel mask to 0x%llx"
- "dcs-channel-enable-mask: 0x%llx\n"
```
