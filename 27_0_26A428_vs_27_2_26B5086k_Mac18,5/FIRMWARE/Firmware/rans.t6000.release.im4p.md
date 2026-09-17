## rans.t6000.release.im4p

> `Firmware/rans.t6000.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_mtab`
- `__TEXT.idle_hooks`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x4580
-  __TEXT.__text: 0x169e40
+  __TEXT.__text: 0x16a0d8
   __TEXT.shared: 0xb964
   __TEXT.read: 0x577c
   __TEXT._rtk_mtab: 0x2f8
-  __TEXT.__const: 0x2dbb0
-  __TEXT.__cstring: 0x1e1d8
+  __TEXT.__const: 0x2e1a0
+  __TEXT.__cstring: 0x1e1a8
   __TEXT.idle_hooks: 0x10
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_power: 0x368
   __DATA._rtk_patchbay: 0x4b8
   __DATA._rtk_tunables: 0x1e8
-  __DATA.__data: 0x7ce8
+  __DATA.__data: 0x7cf0
   __DATA.__const: 0x10638
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x136

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x3fc028
+  __DATA.__zerofill: 0x3fc058
   Functions: 0
   Symbols:   0
-  CStrings:  3305
+  CStrings:  3303
 
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
