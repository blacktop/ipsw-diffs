## rans.t8112.release.im4p

> `Firmware/rans.t8112.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_mtab`
- `__TEXT.idle_hooks`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x44c0
-  __TEXT.__text: 0x178f3c
+  __TEXT.__text: 0x179238
   __TEXT.shared: 0xb20c
   __TEXT.read: 0x58cc
   __TEXT._rtk_mtab: 0x2c8
-  __TEXT.__const: 0x9b18
-  __TEXT.__cstring: 0x1f7fc
+  __TEXT.__const: 0xa108
+  __TEXT.__cstring: 0x1f7cc
   __TEXT.idle_hooks: 0x10
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_power: 0x160
   __DATA._rtk_patchbay: 0x3b8
   __DATA._rtk_tunables: 0x5b0
-  __DATA.__data: 0x72d8
+  __DATA.__data: 0x72e0
   __DATA.__const: 0x1eb8
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x13d

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x2e5208
+  __DATA.__zerofill: 0x2e5238
   Functions: 0
   Symbols:   0
-  CStrings:  3462
+  CStrings:  3460
 
CStrings:
+ "591.40.2"
+ "591.40.2~189"
+ "AppleStorageFirmwarePreASP3-591.40.2~189"
+ "Sanitize Failed"
+ "sanitize cmd drop - not init"
- "591"
- "591~9411"
- "Abort Pad: Flow %u , Band: %u"
- "AppleStorageFirmwarePreASP3-591~9411"
- "Sanitize already in progress, phase=%d"
- "mark band %u"
- "mark band %u, isOpen %u"
```
