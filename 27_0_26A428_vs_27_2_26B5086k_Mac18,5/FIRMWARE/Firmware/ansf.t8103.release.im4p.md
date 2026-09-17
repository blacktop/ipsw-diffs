## ansf.t8103.release.im4p

> `Firmware/ansf.t8103.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_mtab`
- `__TEXT.idle_hooks`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x4580
-  __TEXT.__text: 0x15a254
+  __TEXT.__text: 0x15a5c8
   __TEXT.shared: 0xa4e4
   __TEXT.read: 0x533c
   __TEXT._rtk_mtab: 0x2b0
-  __TEXT.__const: 0xea20
-  __TEXT.__cstring: 0x1dd32
+  __TEXT.__const: 0xf000
+  __TEXT.__cstring: 0x1dd02
   __TEXT.idle_hooks: 0x10
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_power: 0x368
   __DATA._rtk_patchbay: 0x4ac
   __DATA._rtk_tunables: 0x1e8
-  __DATA.__data: 0x7330
+  __DATA.__data: 0x7338
   __DATA.__const: 0x39b8
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x13a

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x2d0a58
+  __DATA.__zerofill: 0x2d0a88
   Functions: 0
   Symbols:   0
-  CStrings:  3240
+  CStrings:  3238
 
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
