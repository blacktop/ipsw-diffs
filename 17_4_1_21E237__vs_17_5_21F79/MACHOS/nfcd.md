## nfcd

> `/usr/libexec/nfcd`

```diff

-344.25.0.0.0
-  __TEXT.__text: 0x23aa94
-  __TEXT.__auth_stubs: 0x1720
-  __TEXT.__objc_stubs: 0xef60
-  __TEXT.__objc_methlist: 0x8498
+345.7.0.0.0
+  __TEXT.__text: 0x23b654
+  __TEXT.__auth_stubs: 0x1730
+  __TEXT.__objc_stubs: 0xef80
+  __TEXT.__objc_methlist: 0x84a0
   __TEXT.__const: 0x1010
-  __TEXT.__oslogstring: 0x22ae8
-  __TEXT.__cstring: 0x2c43b
+  __TEXT.__oslogstring: 0x22af6
+  __TEXT.__cstring: 0x2c38b
   __TEXT.__objc_classname: 0x1a5a
-  __TEXT.__objc_methname: 0x17a16
-  __TEXT.__objc_methtype: 0x5115
-  __TEXT.__gcc_except_tab: 0x4bf0
+  __TEXT.__objc_methname: 0x17a14
+  __TEXT.__objc_methtype: 0x5108
+  __TEXT.__gcc_except_tab: 0x4bbc
   __TEXT.__dlopen_cstrs: 0x549
-  __TEXT.__unwind_info: 0x3454
-  __DATA_CONST.__auth_got: 0xba0
+  __TEXT.__unwind_info: 0x3474
+  __DATA_CONST.__auth_got: 0xba8
   __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0x7430
-  __DATA_CONST.__cfstring: 0xfa00
+  __DATA_CONST.__const: 0x7458
+  __DATA_CONST.__cfstring: 0xf9e0
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x350

   __DATA_CONST.__objc_protorefs: 0x1a0
   __DATA_CONST.__objc_classrefs: 0x7e0
   __DATA_CONST.__objc_superrefs: 0x3d8
-  __DATA_CONST.__objc_intobj: 0x5ee0
+  __DATA_CONST.__objc_intobj: 0x6108
   __DATA_CONST.__objc_arraydata: 0x1dd0
   __DATA_CONST.__objc_arrayobj: 0x3d8
   __DATA_CONST.__objc_dictobj: 0xeb0
   __DATA.__objc_const: 0x164d8
-  __DATA.__objc_selrefs: 0x5658
+  __DATA.__objc_selrefs: 0x5670
   __DATA.__objc_ivar: 0xeec
   __DATA.__objc_data: 0x36b0
   __DATA.__data: 0x2878

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32C525B8-F37F-3C20-B779-A151B298FE11
-  Functions: 4329
-  Symbols:   512
-  CStrings:  14000
+  UUID: 7B994C3F-15AC-3B6C-9F9E-067558CD7CEA
+  Functions: 4334
+  Symbols:   513
+  CStrings:  13997
 
Symbols:
+ _NFIsDarwinOS
CStrings:
+ "%c[%{public}s %{public}s]:%i %{public}@ (%d) started %{public}@ ID:%d %@"
+ "%c[%{public}s %{public}s]:%i Missing associated SSD String info %{public}@"
+ "NFCD built from NF_GIT_CURRENT_BRANCH (NF_GIT_CURRENT_HASH) at 06:49:50 on Apr 13 2024"
+ "^{_NFDriver=i**BBBBBiiiBB{?=ii[10[17C]]QBB}^vBBB}"
+ "_queueFieldDetectProtocolSession:coreNFC:requestor:completion:"
+ "_resume:"
+ "_suspend:"
+ "configureExpressFelicaEntry:"
+ "queueResume"
+ "queueSuspend"
- "%c[%{public}s %{public}s]:%i %{public}@ (%d) started %{public}@ ID:%d"
- "%c[%{public}s %{public}s]:%i Route to passkit; eligibility=%llu"
- "B24@0:8i16B20"
- "Class getFBSDisplayLayoutMonitorClass(void)_block_invoke"
- "Class getFBSDisplayLayoutMonitorConfigurationClass(void)_block_invoke"
- "Client is not foreground"
- "NFCD built from NF_GIT_CURRENT_BRANCH (NF_GIT_CURRENT_HASH) at 00:57:57 on Mar  9 2024"
- "^{_NFDriver=i**BBBBBiiiBB{?=ii[10[17C]]QBB}^vBB}"
- "_checkEligibiltyForPasskitReRouting"
- "_queueFieldDetectProtocolSession:coreNFC:completion:"
- "configureExpressFelicaEntry:andTxEndPatternV2:"
- "void *FrontBoardServicesLibrary(void)"

```
