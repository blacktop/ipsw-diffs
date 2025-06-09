## ptpd

> `/usr/libexec/ptpd`

```diff

-1936.4.3.0.0
-  __TEXT.__text: 0x2df30
+2013.0.0.0.0
+  __TEXT.__text: 0x2d5d4
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_stubs: 0x4700
-  __TEXT.__objc_methlist: 0x2a50
+  __TEXT.__objc_stubs: 0x45a0
+  __TEXT.__objc_methlist: 0x2960
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x6be3
+  __TEXT.__cstring: 0x5b88
   __TEXT.__oslogstring: 0x3f
-  __TEXT.__objc_classname: 0x1fc
-  __TEXT.__objc_methname: 0x62f5
-  __TEXT.__objc_methtype: 0xb66
+  __TEXT.__objc_classname: 0x1f2
+  __TEXT.__objc_methname: 0x6121
+  __TEXT.__objc_methtype: 0xb14
   __TEXT.__ustring: 0xc32
   __TEXT.__gcc_except_tab: 0x5a0
-  __TEXT.__unwind_info: 0x7d0
+  __TEXT.__unwind_info: 0x768
   __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x728
-  __DATA_CONST.__cfstring: 0x77e0
+  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__cfstring: 0x6700
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_intobj: 0x750
-  __DATA_CONST.__objc_arraydata: 0x28e0
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA_CONST.__objc_dictobj: 0x21c0
-  __DATA.__objc_const: 0x3c18
-  __DATA.__objc_selrefs: 0x1af0
-  __DATA.__objc_ivar: 0x40c
+  __DATA.__objc_const: 0x3b48
+  __DATA.__objc_selrefs: 0x1a58
+  __DATA.__objc_ivar: 0x3fc
   __DATA.__objc_data: 0x690
-  __DATA.__data: 0x1c4
-  __DATA.__common: 0x40
-  __DATA.__bss: 0x28
+  __DATA.__data: 0x1b4
+  __DATA.__common: 0x30
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A86D610-FD58-37FB-956D-6EA6541905BE
-  Functions: 984
-  Symbols:   235
-  CStrings:  3420
+  UUID: 2C583820-717D-3B3B-9A51-43E596526DAD
+  Functions: 957
+  Symbols:   233
+  CStrings:  3122
 
Symbols:
+ _ICPreferencesDomain
+ _OBJC_CLASS_$_ICOrderedMediaSet
+ ___ICLogTypeEnabled
+ ___ICOSLogCreate
+ ___ICReadPrefs
+ __gICOSLog
- _CFPreferencesSetMultiple
- _CFPreferencesSynchronize
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSMutableOrderedSet
- _OBJC_CLASS_$_NSProcessInfo
- _kCFPreferencesCurrentHost
- _kCFPreferencesCurrentUser
- _os_log_create
CStrings:
+ "MTPObjectFormatCodeAAC"
+ "MTPObjectFormatCodeAbstractAVPlaylist"
+ "MTPObjectFormatCodeAudible"
+ "MTPObjectFormatCodeDNG"
+ "MTPObjectFormatCodeFLAC"
+ "MTPObjectFormatCodeHEIF"
+ "MTPObjectFormatCodeM3UPlaylist"
+ "MTPObjectFormatCodeMP2"
+ "MTPObjectFormatCodeMP4Container"
+ "MTPObjectFormatCodeOGG"
+ "MTPObjectFormatCodePLSPlaylist"
+ "MTPObjectFormatCodeWMA"
+ "MTPObjectFormatCodeWPLPlaylist"
+ "MTPObjectFormatCodeXMLDocument"
+ "MTPOperationCodeGetPartialObject64"
+ "MTPSetObjectPropValue"
+ "PTPItem"
+ "T"
- "@32@0:8Q16@24"
- "B24@0:8Q16"
- "EEXIST"
- "ENOSPC"
- "EPERM"
- "ICLegacyReturnCodeCannotYieldDevice"
- "ICLegacyReturnCodeCommunicationErr"
- "ICLegacyReturnCodeDataTypeNotFoundErr"
- "ICLegacyReturnCodeDeviceAlreadyOpenErr"
- "ICLegacyReturnCodeDeviceIOServicePathNotFoundErr"
- "ICLegacyReturnCodeDeviceInternalErr"
- "ICLegacyReturnCodeDeviceInvalidParamErr"
- "ICLegacyReturnCodeDeviceLocationIDNotFoundErr"
- "ICLegacyReturnCodeDeviceMemoryAllocationErr"
- "ICLegacyReturnCodeDeviceNotFoundErr"
- "ICLegacyReturnCodeDeviceNotOpenErr"
- "ICLegacyReturnCodeDeviceUnsupportedErr"
- "ICLegacyReturnCodeExtensionInternalErr"
- "ICLegacyReturnCodeFileCorruptedErr"
- "ICLegacyReturnCodeFrameworkInternalErr"
- "ICLegacyReturnCodeIOPendingErr"
- "ICLegacyReturnCodeIndexOutOfRangeErr"
- "ICLegacyReturnCodeInvalidObjectErr"
- "ICLegacyReturnCodeInvalidPropertyErr"
- "ICLegacyReturnCodeInvalidSessionErr"
- "ICLegacyReturnCodePropertyTypeNotFoundErr"
- "ICOrderedMediaSet"
- "ICReturnCommunicationTimedOut"
- "ICReturnConnectionFailedToOpen"
- "ICReturnDeleteFilesCanceled"
- "ICReturnDeleteFilesFailed"
- "ICReturnDeviceCommandGeneralFailure"
- "ICReturnDeviceCouldNotPair"
- "ICReturnDeviceFailedToCloseSession"
- "ICReturnDeviceFailedToCompleteTransfer"
- "ICReturnDeviceFailedToOpenSession"
- "ICReturnDeviceFailedToSendData"
- "ICReturnDeviceFailedToTakePicture"
- "ICReturnDeviceIsBusyEnumerating"
- "ICReturnDeviceIsPasscodeLocked"
- "ICReturnDeviceNeedsCredentials"
- "ICReturnDeviceSoftwareInstallationCanceled"
- "ICReturnDeviceSoftwareInstallationCompleted"
- "ICReturnDeviceSoftwareInstallationFailed"
- "ICReturnDeviceSoftwareIsBeingInstalled"
- "ICReturnDeviceSoftwareNotAvailable"
- "ICReturnDeviceSoftwareNotInstalled"
- "ICReturnDownloadCanceled"
- "ICReturnDownloadFailed"
- "ICReturnFailedToCompletePassThroughCommand"
- "ICReturnFailedToCompleteSendMessageRequest"
- "ICReturnFailedToDisabeTethering"
- "ICReturnFailedToDisableTethering"
- "ICReturnFailedToEnabeTethering"
- "ICReturnFailedToEnableTethering"
- "ICReturnInvalidParam"
- "ICReturnReceivedUnsolicitedScannerStatusInfo"
- "ICReturnScanOperationCanceled"
- "ICReturnScannerFailedToCompleteOverviewScan"
- "ICReturnScannerFailedToCompleteScan"
- "ICReturnScannerFailedToSelectFunctionalUnit"
- "ICReturnScannerInUseByLocalUser"
- "ICReturnScannerInUseByRemoteUser"
- "ICReturnSessionNotOpened"
- "ICReturnUploadFailed"
- "KERN_NO_ACCESS"
- "T@\"NSMutableDictionary\",&,N,V_mediaItems"
- "T{os_unfair_lock_s=I},N,V_mediaLock"
- "[IOReturn.h] _device iokit channel busy."
- "[IOReturn.h] _device iokit timeout."
- "[MacErrors.h] _device call unimplemented."
- "[MacErrors.h] _device parameter invalid."
- "[MacErrors.h] _file not found."
- "[MacErrors.h] _scanner has too many clients."
- "[MacErrors.h] _user operation canceled."
- "[errno.h] _device out of space."
- "[errno.h] _file already exists."
- "[errno.h] _file operation not permitted."
- "[kern_return.h] _kernel reurned no access."
- "_appledevice is locked or unpaired."
- "_appledevice pairing failed."
- "_appledevice unpairing failed."
- "_camera delete files canceled."
- "_camera delete files failed."
- "_camera disable tethering failed."
- "_camera enable tethering failed."
- "_camera failed to take picture."
- "_camera is enumerating content."
- "_camera passthru command failed."
- "_camera received incorrect data size."
- "_camera send data failed."
- "_device IO Pending."
- "_device already open."
- "_device can't allocate memory."
- "_device close session failed."
- "_device command failed."
- "_device communication error."
- "_device download canceled."
- "_device download failed."
- "_device fw GUID invalid."
- "_device internal error."
- "_device ioservice path invalid."
- "_device module XPC communication failed."
- "_device not found."
- "_device not open."
- "_device open session failed."
- "_device parameter invalid."
- "_device send message failed."
- "_device session invalid."
- "_device session not open."
- "_device unsupported."
- "_device upload failed."
- "_device usb location ID invalid. "
- "_device won't yield."
- "_file corrupted."
- "_framework internal error."
- "_mediaItems"
- "_mediaLock"
- "_module communication timed out."
- "_module parameter invalid"
- "_object data type not found."
- "_object index out of range."
- "_object invalid."
- "_object property invalid."
- "_object property type invalid."
- "_obsolete | _device software install canceled."
- "_obsolete | _device software install failed."
- "_obsolete | _device software installed."
- "_obsolete | _device software installing."
- "_obsolete | _device software not available."
- "_obsolete | _device software not installed."
- "_obsoleted"
- "_operation success."
- "_scaner action canceled."
- "_scanner functional unit selection failed."
- "_scanner in use locally."
- "_scanner in use remotely."
- "_scanner overview scan failed."
- "_scanner reported unsolicited error."
- "_scanner reported unsolicited status."
- "_scanner requested scan failed."
- "_uscandevice needs credentials."
- "arrayForType:"
- "com.apple.ImageCaptureFramework"
- "dictionaryWithDictionary:"
- "fBsyErr"
- "fnfErr"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "insertObject:atIndex:"
- "kICASandboxViolation"
- "kICASecureSessionRequired"
- "kIOReturnBusy"
- "kIOReturnTimeout"
- "legacy"
- "loggingLevel"
- "mediaItemCount"
- "mediaItems"
- "mediaLock"
- "modern"
- "numberWithUnsignedInteger:"
- "orderedSet"
- "orderedSetForType:"
- "paramErr"
- "performSelector:onTypes:"
- "processInfo"
- "processName"
- "q24@?0@\"<ICMediaItemProtocol>\"8@\"<ICMediaItemProtocol>\"16"
- "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
- "removeAllItems"
- "removeMediaItemFromIndex:"
- "removeMediaItemsFromIndex:"
- "removeObject:"
- "setMediaItems:"
- "setMediaLock:"
- "success"
- "text"
- "unimpErr"
- "userCanceledErr"
- "v20@0:8{os_unfair_lock_s=I}16"
- "{os_unfair_lock_s=I}16@0:8"
- "\x81"

```
