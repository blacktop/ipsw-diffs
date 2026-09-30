## rans.t8122.release.im4p

> `Firmware/rans.t8122.release.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_mtab`
- `__TEXT.idle_hooks`
- `__DATA.__const`

```diff

   __TEXT.text_first: 0x44c0
-  __TEXT.__text: 0x18dd80
+  __TEXT.__text: 0x18e098
   __TEXT.shared: 0xcb5c
   __TEXT.read: 0x60dc
   __TEXT._rtk_mtab: 0x540
-  __TEXT.__const: 0x9d78
-  __TEXT.__cstring: 0x1fd94
+  __TEXT.__const: 0xa368
+  __TEXT.__cstring: 0x1fd64
   __TEXT.idle_hooks: 0x10
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA._rtk_power: 0x160
   __DATA._rtk_patchbay: 0x3c4
   __DATA._rtk_tunables: 0x5b0
-  __DATA.__data: 0x7d54
+  __DATA.__data: 0x7d5c
   __DATA.__const: 0x2218
   __DATA.__gxf_data: 0x10
   __DATA.core_globals: 0x13f

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x318c28
+  __DATA.__zerofill: 0x318c58
   Functions: 0
   Symbols:   0
-  CStrings:  3507
+  CStrings:  3505
 
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
