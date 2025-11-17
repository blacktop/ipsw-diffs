## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2180.3.1.0.0
-  __TEXT.__text: 0x79a5e8
-  __TEXT.__auth_stubs: 0x5630
-  __TEXT.__objc_methlist: 0x35d08
+2180.4.1.1.0
+  __TEXT.__text: 0x79ac50
+  __TEXT.__auth_stubs: 0x5640
+  __TEXT.__objc_methlist: 0x35d10
   __TEXT.__const: 0xc780
-  __TEXT.__cstring: 0x8fa2e
-  __TEXT.__oslogstring: 0x10fbed
+  __TEXT.__cstring: 0x8fa87
+  __TEXT.__oslogstring: 0x10fdba
   __TEXT.__gcc_except_tab: 0x2b44
   __TEXT.__ustring: 0x2d4
   __TEXT.__unwind_info: 0x10928
   __TEXT.__objc_classname: 0x4ed7
-  __TEXT.__objc_methname: 0x7e17f
+  __TEXT.__objc_methname: 0x7e1cf
   __TEXT.__objc_methtype: 0x283d7
-  __TEXT.__objc_stubs: 0x4f0e0
+  __TEXT.__objc_stubs: 0x4f100
   __DATA_CONST.__got: 0x1a60
   __DATA_CONST.__const: 0x6b38
   __DATA_CONST.__objc_classlist: 0x12f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16a98
+  __DATA_CONST.__objc_selrefs: 0x16aa0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
-  __AUTH_CONST.__auth_got: 0x2b30
+  __AUTH_CONST.__auth_got: 0x2b38
   __AUTH_CONST.__const: 0x3ca8
-  __AUTH_CONST.__cfstring: 0x265c0
-  __AUTH_CONST.__objc_const: 0x63a30
+  __AUTH_CONST.__cfstring: 0x265e0
+  __AUTH_CONST.__objc_const: 0x63a70
   __AUTH_CONST.__objc_intobj: 0x4a10
   __AUTH_CONST.__objc_arrayobj: 0x1b48
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_ivar: 0x6cd0
+  __DATA.__objc_ivar: 0x6cd8
   __DATA.__data: 0x78b0
   __DATA.__bss: 0xd78
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C7A0CB42-0887-3CF1-9137-AEC0F1465669
-  Functions: 31654
-  Symbols:   97609
-  CStrings:  57380
+  UUID: B20B5AB7-5693-3DAE-B0A1-C1DA28C6C1A5
+  Functions: 31656
+  Symbols:   97617
+  CStrings:  57390
 
Symbols:
+ -[VCSession updateL4SModeWithNewPrimaryConnection:]
+ -[VCSession updateL4SModeWithNewPrimaryConnection:].cold.1
+ -[VCSession updateL4SModeWithNewPrimaryConnection:].cold.2
+ GCC_except_table204
+ _OBJC_IVAR_$_VCSession._previousECNEnabled
+ _OBJC_IVAR_$_VCSession._previousECNLinkType
+ _nw_interface_get_l4s_mode
+ _objc_msgSend$updateL4SModeWithNewPrimaryConnection:
- GCC_except_table203
CStrings:
+ "-[VCSession updateL4SModeWithNewPrimaryConnection:]"
+ "2180.4.1.1"
+ "VCSession [%s] %s:%d Get nw interface l4sMode=%d on interface=%@ (%p), ecnLinkType=%d, isECNEnabled=%d, isECNCapable=%d"
+ "VCSession [%s] %s:%d L4S Mode not updated with isECNCapable=%d, newPrimary=%p"
+ "VCSession [%s] %s:%d Primary connection changed to interface %@ and set to previous ECNEnable=%d, from ecnLinkType=%d to new ecnLinkType=%d"
+ "VCSession [%s] %s:%d Primary connection changed to interface %@ with l4sMode=%d, from ecnLinkType=%d to new ecnLinkType=%d"
+ "_previousECNEnabled"
+ "_previousECNLinkType"
+ "forceDisableAudioPlayerAdaptations"
+ "updateL4SModeWithNewPrimaryConnection:"
- "2180.3.1"

```
