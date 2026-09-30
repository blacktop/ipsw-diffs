## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5409.0.0.0.0
-  __TEXT.__text: 0x44824
-  __TEXT.__objc_methlist: 0x41b4
+5411.0.0.0.0
+  __TEXT.__text: 0x44ac4
+  __TEXT.__objc_methlist: 0x420c
   __TEXT.__const: 0x140
   __TEXT.__gcc_except_tab: 0xf4c
-  __TEXT.__oslogstring: 0x59f4
-  __TEXT.__cstring: 0x34e3
+  __TEXT.__oslogstring: 0x5a31
+  __TEXT.__cstring: 0x3511
   __TEXT.__dlopen_cstrs: 0x13dd
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x1360
+  __TEXT.__unwind_info: 0x1368
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1778
+  __DATA_CONST.__const: 0x1780
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c88
+  __DATA_CONST.__objc_selrefs: 0x2cb0
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x178
   __DATA_CONST.__got: 0x540
-  __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x3ae0
-  __AUTH_CONST.__objc_const: 0x62d0
+  __AUTH_CONST.__const: 0xac0
+  __AUTH_CONST.__cfstring: 0x3b00
+  __AUTH_CONST.__objc_const: 0x6308
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x10e0
-  __DATA.__objc_ivar: 0x3d0
+  __DATA.__objc_ivar: 0x3d4
   __DATA.__data: 0xa90
   __DATA.__bss: 0x648
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1801
-  Symbols:   4218
-  CStrings:  1138
+  Functions: 1807
+  Symbols:   4231
+  CStrings:  1140
 
Symbols:
+ +[BYChronicleEntry osVersionIsAorERelease:]
+ -[BYBuddyDaemonGeneralClient beginServicesTermsRequirementCheck]
+ -[BYChronicleEntry hasCrossedAOrEBoundary]
+ -[BYManagedAppleIDBootstrap cachedManagedAccountAltDSID]
+ -[BYManagedAppleIDBootstrap setCachedManagedAccountAltDSID:]
+ _BYSetupAssistantDidCompleteAppleAccountNotification
+ _OBJC_IVAR_$_BYManagedAppleIDBootstrap._cachedManagedAccountAltDSID
+ __OBJC_$_CLASS_METHODS_BYChronicleEntry
+ ___64-[BYBuddyDaemonGeneralClient beginServicesTermsRequirementCheck]_block_invoke
+ _objc_msgSend$beginServicesTermsRequirementCheck
+ _objc_msgSend$cachedManagedAccountAltDSID
+ _objc_msgSend$createdOnCurrentMajorVersion
+ _objc_msgSend$hasCrossedEBoundarySinceCreationForCurrentProductVersion:
+ _objc_msgSend$setCachedManagedAccountAltDSID:
- GCC_except_table53
CStrings:
+ "Failed to begin services terms requirement check: %{public}@"
+ "com.apple.purplebuddy.didcompleteappleaccount"
```
