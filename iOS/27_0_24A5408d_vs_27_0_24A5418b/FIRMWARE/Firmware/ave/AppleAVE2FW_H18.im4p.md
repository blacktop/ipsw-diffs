## AppleAVE2FW_H18.im4p

> `Firmware/ave/AppleAVE2FW_H18.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`

```diff

-  __TEXT.__text: 0x117224
+  __TEXT.__text: 0x1172a4
   __TEXT.__const: 0x17084
-  __TEXT.__cstring: 0x197f7
+  __TEXT.__cstring: 0x19815
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211

   __DATA.__zerofill: 0xc6860
   Functions: 1290
   Symbols:   1793
-  CStrings:  2863
+  CStrings:  2864
 
Functions:
~ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb : 236 -> 344
~ __Z20AVE_IOP_Config_pandav : 352 -> 348
~ _exp2f : 168 -> 176
~ _pow : 1200 -> 1216
CStrings:
+ "9013.45.2"
+ "Applying gating for frame: %d"
- "9013.45.1"
```
