## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-2718.0.12.0.0
-  __TEXT.__text: 0x29a1c
+2718.0.18.0.0
+  __TEXT.__text: 0x29b5c
   __TEXT.__auth_stubs: 0x1650
-  __TEXT.__objc_stubs: 0x3780
-  __TEXT.__objc_methlist: 0x1714
-  __TEXT.__cstring: 0x1170b
+  __TEXT.__objc_stubs: 0x37c0
+  __TEXT.__objc_methlist: 0x172c
+  __TEXT.__cstring: 0x117b9
   __TEXT.__const: 0x1218
-  __TEXT.__gcc_except_tab: 0x540
-  __TEXT.__objc_methname: 0x3c3b
+  __TEXT.__gcc_except_tab: 0x54c
+  __TEXT.__objc_methname: 0x3c82
   __TEXT.__objc_classname: 0x1b7
   __TEXT.__objc_methtype: 0xe04
   __TEXT.__oslogstring: 0x1c6
-  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__unwind_info: 0x8e8
   __DATA_CONST.__const: 0x1670
-  __DATA_CONST.__cfstring: 0xaaa0
+  __DATA_CONST.__cfstring: 0xab60
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0xb38
-  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__got: 0x300
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x1fa0
-  __DATA.__objc_selrefs: 0x1168
+  __DATA.__objc_selrefs: 0x1180
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x4e0

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 819
-  Symbols:   2215
-  CStrings:  2990
+  Functions: 821
+  Symbols:   2220
+  CStrings:  2999
 
Symbols:
+ +[MSUBootFirmwareUpdater hasExclusiveUSBHostDeviceMode]
+ -[UMEventRecorder _getCoalescedSubTargetID]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-47848c4b75f88441f64bf663032c47e0.o
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-975c7d4158e0ac13103afc2974f458a2.o
+ GCC_except_table27
+ _OBJC_CLASS_$_NSSet
+ _objc_msgSend$_getCoalescedSubTargetID
+ _objc_msgSend$setWithObjects:
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-3706ebc2097927ad32ceb88b9a080fef.o
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/MobileSoftwareUpdate/install/TempContent/Objects/MobileSoftwareUpdate.build/CleanupPreparePathService.build/Objects-normal/arm64e/common-d1673c0c16fe748c195b69493adf3aaf.o
- GCC_except_table26
Functions:
~ _saveAccessibilityDomainsForDRE : 904 -> 1044
~ _submitRestoreLogFileToLogDir : 2600 -> 2656
~ _legacyInstallInfoFileWithDataMountPoint : 76 -> 72
~ -[UMEventRecorder _recordEvent:getPowerLog:information:callback:] : 2008 -> 2040
+ -[UMEventRecorder _getCoalescedSubTargetID]
+ +[MSUBootFirmwareUpdater hasExclusiveUSBHostDeviceMode]
CStrings:
+ "AXSVoiceOverTurnOnBluetoothEnabled"
+ "CoalescedSubTargetID"
+ "Skipping denied accessibility key: %@ in domain: %@\n"
+ "_getCoalescedSubTargetID"
+ "coalescedSubTargetID"
+ "hasExclusiveUSBHostDeviceMode"
+ "setWithObjects:"
+ "target_os_version"
+ "usb-host-device-exclusive"
```
