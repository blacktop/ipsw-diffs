## com.apple.accessoryd.matching

> `/System/Library/UserEventPlugins/com.apple.accessoryd.matching.plugin/com.apple.accessoryd.matching`

```diff

-1139.40.1.0.0
-  __TEXT.__text: 0x386a0
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x47c0
-  __TEXT.__objc_methlist: 0x1e84
-  __TEXT.__cstring: 0x488c
-  __TEXT.__objc_methname: 0x620c
-  __TEXT.__objc_classname: 0x26c
-  __TEXT.__objc_methtype: 0xaaa
-  __TEXT.__const: 0x200
-  __TEXT.__oslogstring: 0x3b68
-  __TEXT.__gcc_except_tab: 0x4a4
+1139.40.6.0.0
+  __TEXT.__text: 0x3b984
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_stubs: 0x4e00
+  __TEXT.__objc_methlist: 0x237c
+  __TEXT.__cstring: 0x4994
+  __TEXT.__objc_methname: 0x6da0
+  __TEXT.__objc_classname: 0x2b5
+  __TEXT.__objc_methtype: 0xada
+  __TEXT.__const: 0x218
+  __TEXT.__oslogstring: 0x3f3e
+  __TEXT.__gcc_except_tab: 0x550
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x918
-  __DATA.__auth_got: 0x800
-  __DATA.__got: 0x2f0
+  __TEXT.__unwind_info: 0x9f0
+  __DATA.__auth_got: 0x810
+  __DATA.__got: 0x340
   __DATA.__auth_ptr: 0x18
-  __DATA.__const: 0xf00
-  __DATA.__cfstring: 0x3600
-  __DATA.__objc_classlist: 0x98
+  __DATA.__const: 0x1030
+  __DATA.__cfstring: 0x36a0
+  __DATA.__objc_classlist: 0xb0
   __DATA.__objc_catlist: 0x10
   __DATA.__objc_protolist: 0x48
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x33c8
-  __DATA.__objc_selrefs: 0x1748
+  __DATA.__objc_const: 0x3c80
+  __DATA.__objc_selrefs: 0x19c0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0x2fc
-  __DATA.__objc_data: 0x5f0
+  __DATA.__objc_superrefs: 0xa8
+  __DATA.__objc_ivar: 0x388
+  __DATA.__objc_data: 0x6e0
   __DATA.__objc_arraydata: 0xe8
   __DATA.__objc_arrayobj: 0x90
   __DATA.__objc_intobj: 0x60
   __DATA.__data: 0x39e
   __DATA.__objc_dictobj: 0x28
-  __DATA.__bss: 0x1b8
+  __DATA.__bss: 0x1d8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libIOAccessoryManager.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 516E7C51-6536-32AA-B78A-9BF257B5D45A
-  Functions: 1286
-  Symbols:   7303
-  CStrings:  2745
+  UUID: 60E89406-04C3-3752-A560-895967A84980
+  Functions: 1423
+  Symbols:   8168
+  CStrings:  2917
 
Symbols:
+ +[IOUserNotification _findCFUserNotificationForUserNotification:]
+ +[IOUserNotification _notificationMapTableLock]
+ +[IOUserNotification _notificationMapTableLock].cold.1
+ +[IOUserNotification _notificationMapTable]
+ +[IOUserNotification _notificationMapTable].cold.1
+ +[IOUserNotification notificationWithHeader:andMessage:]
+ +[IOUserNotificationButton buttonWithTitle:]
+ +[IOUserNotificationOption optionWithTitle:selected:]
+ -[IOUserNotification .cxx_destruct]
+ -[IOUserNotification _addButton:]
+ -[IOUserNotification _addOption:]
+ -[IOUserNotification _userNotificationDictionary]
+ -[IOUserNotification _userNotificationDictionary].cold.1
+ -[IOUserNotification _userNotificationOptionFlags]
+ -[IOUserNotification addButtonWithTitle:]
+ -[IOUserNotification addOptionWithTitle:selected:]
+ -[IOUserNotification additionalConfiguration]
+ -[IOUserNotification buttonsMutable]
+ -[IOUserNotification buttons]
+ -[IOUserNotification dealloc]
+ -[IOUserNotification description]
+ -[IOUserNotification dismissNotification]
+ -[IOUserNotification extensionIdentifier]
+ -[IOUserNotification extensionItems]
+ -[IOUserNotification header]
+ -[IOUserNotification iconConfiguration]
+ -[IOUserNotification iconURL]
+ -[IOUserNotification initWithHeader:andMessage:]
+ -[IOUserNotification init]
+ -[IOUserNotification isVisible]
+ -[IOUserNotification lockScreenHeader]
+ -[IOUserNotification lockScreenMessage]
+ -[IOUserNotification message]
+ -[IOUserNotification noDefaultButton]
+ -[IOUserNotification notificationCancelled]
+ -[IOUserNotification notificationDismissed]
+ -[IOUserNotification notificationLevel]
+ -[IOUserNotification optionsMutable]
+ -[IOUserNotification options]
+ -[IOUserNotification presentNotificationWithResponseHandler:]
+ -[IOUserNotification presentNotification]
+ -[IOUserNotification queue]
+ -[IOUserNotification responseHandler]
+ -[IOUserNotification responseReceived]
+ -[IOUserNotification response]
+ -[IOUserNotification setAdditionalConfiguration:]
+ -[IOUserNotification setButtonsMutable:]
+ -[IOUserNotification setExtensionIdentifier:]
+ -[IOUserNotification setExtensionItems:]
+ -[IOUserNotification setHeader:]
+ -[IOUserNotification setIconConfiguration:]
+ -[IOUserNotification setIconURL:]
+ -[IOUserNotification setLockScreenHeader:]
+ -[IOUserNotification setLockScreenMessage:]
+ -[IOUserNotification setMessage:]
+ -[IOUserNotification setNoDefaultButton:]
+ -[IOUserNotification setNotificationCancelled:]
+ -[IOUserNotification setNotificationDismissed:]
+ -[IOUserNotification setNotificationLevel:]
+ -[IOUserNotification setOptionsMutable:]
+ -[IOUserNotification setQueue:]
+ -[IOUserNotification setResponse:]
+ -[IOUserNotification setResponseHandler:]
+ -[IOUserNotification setResponseReceived:]
+ -[IOUserNotification setShouldAllowLockScreenDismissal:]
+ -[IOUserNotification setShouldDismissOnLock:]
+ -[IOUserNotification setShouldDismissOnUnlock:]
+ -[IOUserNotification setShouldDisplayOnTop:]
+ -[IOUserNotification setShouldHideOnMirroredDisplay:]
+ -[IOUserNotification setShouldIgnoreQuietMode:]
+ -[IOUserNotification setShouldPresentViaSystemAperture:]
+ -[IOUserNotification setSystemSoundID:]
+ -[IOUserNotification setTimeout:]
+ -[IOUserNotification setUpdateCount:]
+ -[IOUserNotification setUseRadioOptions:]
+ -[IOUserNotification setVisible:]
+ -[IOUserNotification shouldAllowLockScreenDismissal]
+ -[IOUserNotification shouldDismissOnLock]
+ -[IOUserNotification shouldDismissOnUnlock]
+ -[IOUserNotification shouldDisplayOnTop]
+ -[IOUserNotification shouldHideOnMirroredDisplay]
+ -[IOUserNotification shouldIgnoreQuietMode]
+ -[IOUserNotification shouldPresentViaSystemAperture]
+ -[IOUserNotification systemSoundID]
+ -[IOUserNotification timeout]
+ -[IOUserNotification updateCount]
+ -[IOUserNotification updateNotification]
+ -[IOUserNotification useRadioOptions]
+ -[IOUserNotificationButton .cxx_destruct]
+ -[IOUserNotificationButton description]
+ -[IOUserNotificationButton initWithTitle:]
+ -[IOUserNotificationButton init]
+ -[IOUserNotificationButton selected]
+ -[IOUserNotificationButton setSelected:]
+ -[IOUserNotificationButton setTitle:]
+ -[IOUserNotificationButton title]
+ -[IOUserNotificationOption .cxx_destruct]
+ -[IOUserNotificationOption description]
+ -[IOUserNotificationOption initWithTitle:selected:]
+ -[IOUserNotificationOption init]
+ -[IOUserNotificationOption selected]
+ -[IOUserNotificationOption setSelected:]
+ -[IOUserNotificationOption setTitle:]
+ -[IOUserNotificationOption title]
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessorydMatchingPlugin.build/Objects-normal/arm64e/IOUserNotification.o
+ GCC_except_table10
+ GCC_except_table15
+ GCC_except_table25
+ GCC_except_table259
+ IOUserNotification.m
+ OBJC_IVAR_$_IOUserNotification._additionalConfiguration
+ OBJC_IVAR_$_IOUserNotification._buttonsMutable
+ OBJC_IVAR_$_IOUserNotification._extensionIdentifier
+ OBJC_IVAR_$_IOUserNotification._extensionItems
+ OBJC_IVAR_$_IOUserNotification._header
+ OBJC_IVAR_$_IOUserNotification._iconConfiguration
+ OBJC_IVAR_$_IOUserNotification._iconURL
+ OBJC_IVAR_$_IOUserNotification._lockScreenHeader
+ OBJC_IVAR_$_IOUserNotification._lockScreenMessage
+ OBJC_IVAR_$_IOUserNotification._message
+ OBJC_IVAR_$_IOUserNotification._noDefaultButton
+ OBJC_IVAR_$_IOUserNotification._notificationCancelled
+ OBJC_IVAR_$_IOUserNotification._notificationDismissed
+ OBJC_IVAR_$_IOUserNotification._notificationLevel
+ OBJC_IVAR_$_IOUserNotification._optionsMutable
+ OBJC_IVAR_$_IOUserNotification._queue
+ OBJC_IVAR_$_IOUserNotification._response
+ OBJC_IVAR_$_IOUserNotification._responseHandler
+ OBJC_IVAR_$_IOUserNotification._responseReceived
+ OBJC_IVAR_$_IOUserNotification._shouldAllowLockScreenDismissal
+ OBJC_IVAR_$_IOUserNotification._shouldDismissOnLock
+ OBJC_IVAR_$_IOUserNotification._shouldDismissOnUnlock
+ OBJC_IVAR_$_IOUserNotification._shouldDisplayOnTop
+ OBJC_IVAR_$_IOUserNotification._shouldHideOnMirroredDisplay
+ OBJC_IVAR_$_IOUserNotification._shouldIgnoreQuietMode
+ OBJC_IVAR_$_IOUserNotification._shouldPresentViaSystemAperture
+ OBJC_IVAR_$_IOUserNotification._systemSoundID
+ OBJC_IVAR_$_IOUserNotification._timeout
+ OBJC_IVAR_$_IOUserNotification._updateCount
+ OBJC_IVAR_$_IOUserNotification._useRadioOptions
+ OBJC_IVAR_$_IOUserNotification._visible
+ OBJC_IVAR_$_IOUserNotificationButton._selected
+ OBJC_IVAR_$_IOUserNotificationButton._title
+ OBJC_IVAR_$_IOUserNotificationOption._selected
+ OBJC_IVAR_$_IOUserNotificationOption._title
+ RegulatoryDomainChanged.cold.1
+ _CFRunLoopAddSource
+ _CFUserNotificationCreateRunLoopSource
+ _IOUserNotificationErrorDomain
+ _OBJC_CLASS_$_IOUserNotification
+ _OBJC_CLASS_$_IOUserNotificationButton
+ _OBJC_CLASS_$_IOUserNotificationOption
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_RDEstimate
+ _OBJC_METACLASS_$_IOUserNotification
+ _OBJC_METACLASS_$_IOUserNotificationButton
+ _OBJC_METACLASS_$_IOUserNotificationOption
+ _RegulatoryDomainChanged
+ _SBUserNotificationExtensionIdentifierKey
+ _SBUserNotificationExtensionItemsKey
+ _SBUserNotificationHideOnClonedDisplay
+ __33-[IOUserNotification _addButton:]_block_invoke.cold.1
+ __33-[IOUserNotification _addOption:]_block_invoke.cold.1
+ __40-[IOUserNotification updateNotification]_block_invoke.20
+ __40-[IOUserNotification updateNotification]_block_invoke.20.cold.1
+ __41-[IOUserNotification dismissNotification]_block_invoke.21
+ __41-[IOUserNotification dismissNotification]_block_invoke.21.cold.1
+ __41-[IOUserNotification dismissNotification]_block_invoke.22
+ __41-[IOUserNotification dismissNotification]_block_invoke.22.cold.1
+ __41-[IOUserNotification dismissNotification]_block_invoke.cold.1
+ __41-[IOUserNotification presentNotification]_block_invoke.13
+ __41-[IOUserNotification presentNotification]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_IOUserNotification
+ __OBJC_$_CLASS_METHODS_IOUserNotificationButton
+ __OBJC_$_CLASS_METHODS_IOUserNotificationOption
+ __OBJC_$_CLASS_PROP_LIST_IOUserNotification
+ __OBJC_$_INSTANCE_METHODS_IOUserNotification
+ __OBJC_$_INSTANCE_METHODS_IOUserNotificationButton
+ __OBJC_$_INSTANCE_METHODS_IOUserNotificationOption
+ __OBJC_$_INSTANCE_VARIABLES_IOUserNotification
+ __OBJC_$_INSTANCE_VARIABLES_IOUserNotificationButton
+ __OBJC_$_INSTANCE_VARIABLES_IOUserNotificationOption
+ __OBJC_$_PROP_LIST_IOUserNotification
+ __OBJC_$_PROP_LIST_IOUserNotificationButton
+ __OBJC_$_PROP_LIST_IOUserNotificationOption
+ __OBJC_CLASS_RO_$_IOUserNotification
+ __OBJC_CLASS_RO_$_IOUserNotificationButton
+ __OBJC_CLASS_RO_$_IOUserNotificationOption
+ __OBJC_METACLASS_RO_$_IOUserNotification
+ __OBJC_METACLASS_RO_$_IOUserNotificationButton
+ __OBJC_METACLASS_RO_$_IOUserNotificationOption
+ ___33-[IOUserNotification _addButton:]_block_invoke
+ ___33-[IOUserNotification _addOption:]_block_invoke
+ ___40-[IOUserNotification updateNotification]_block_invoke
+ ___41-[IOUserNotification dismissNotification]_block_invoke
+ ___41-[IOUserNotification presentNotification]_block_invoke
+ ___43+[IOUserNotification _notificationMapTable]_block_invoke
+ ___47+[IOUserNotification _notificationMapTableLock]_block_invoke
+ ___50-[IOUserNotification _userNotificationOptionFlags]_block_invoke
+ ____userNotificationCallback_block_invoke
+ ____userNotificationCallback_block_invoke_2
+ ___block_descriptor_40_e41_v32?0"IOUserNotificationOption"8Q16^B24l
+ ___block_descriptor_40_e8_32r_e41_v32?0"IOUserNotificationOption"8Q16^B24lr32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ __block_literal_global.29
+ __block_literal_global.915
+ __block_literal_global.918
+ __block_literal_global.920
+ __block_literal_global.923
+ __block_literal_global.935
+ __block_literal_global.937
+ __checkFor128KHzRestriction
+ __serviceLDCMMitigationStatusChanged_block_invoke.916
+ __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.1
+ __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.2
+ __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.3
+ __serviceLDCMMitigationStatusChanged_block_invoke.916.cold.4
+ __userNotificationCallback
+ _checkFor128KHzRestriction.cold.1
+ _checkFor128KHzRestriction.cold.2
+ _checkFor128KHzRestriction.cold.3
+ _checkFor128KHzRestriction.cold.4
+ _checkFor128KHzRestriction.cold.5
+ _checkFor128KHzRestriction.cold.6
+ _checkFor128KHzRestriction.cold.7
+ _kCFRunLoopCommonModes
+ _kCFUserNotificationCheckBoxTitlesKey
+ _kCFUserNotificationIconURLKey
+ _kCFUserNotificationOtherButtonTitleKey
+ _kRegulatoryDomainUpdateNotification
+ _notificationMapTable.mapTable
+ _notificationMapTable.onceToken
+ _notificationMapTableLock.lock
+ _notificationMapTableLock.onceToken
+ _objc_msgSend$_addButton:
+ _objc_msgSend$_addOption:
+ _objc_msgSend$_findCFUserNotificationForUserNotification:
+ _objc_msgSend$_notificationMapTable
+ _objc_msgSend$_notificationMapTableLock
+ _objc_msgSend$_userNotificationDictionary
+ _objc_msgSend$_userNotificationOptionFlags
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$additionalConfiguration
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$buttonWithTitle:
+ _objc_msgSend$buttonsMutable
+ _objc_msgSend$countryCode
+ _objc_msgSend$currentEstimates
+ _objc_msgSend$dismissNotification
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$extensionIdentifier
+ _objc_msgSend$extensionItems
+ _objc_msgSend$header
+ _objc_msgSend$iconURL
+ _objc_msgSend$initWithHeader:andMessage:
+ _objc_msgSend$initWithTitle:
+ _objc_msgSend$initWithTitle:selected:
+ _objc_msgSend$isVisible
+ _objc_msgSend$lastKnownEstimates
+ _objc_msgSend$lockScreenHeader
+ _objc_msgSend$noDefaultButton
+ _objc_msgSend$notificationLevel
+ _objc_msgSend$optionWithTitle:selected:
+ _objc_msgSend$optionsMutable
+ _objc_msgSend$pointerValue
+ _objc_msgSend$presentNotification
+ _objc_msgSend$responseHandler
+ _objc_msgSend$selected
+ _objc_msgSend$setNotificationCancelled:
+ _objc_msgSend$setNotificationDismissed:
+ _objc_msgSend$setResponse:
+ _objc_msgSend$setResponseHandler:
+ _objc_msgSend$setResponseReceived:
+ _objc_msgSend$setSelected:
+ _objc_msgSend$setVisible:
+ _objc_msgSend$shouldAllowLockScreenDismissal
+ _objc_msgSend$shouldDismissOnLock
+ _objc_msgSend$shouldDismissOnUnlock
+ _objc_msgSend$shouldDisplayOnTop
+ _objc_msgSend$shouldHideOnMirroredDisplay
+ _objc_msgSend$shouldIgnoreQuietMode
+ _objc_msgSend$shouldPresentViaSystemAperture
+ _objc_msgSend$useRadioOptions
+ _objc_msgSend$valueWithPointer:
+ _userNotificationCallback.cold.1
+ _userNotificationCallback.cold.2
- GCC_except_table257
- __block_literal_global.911
- __block_literal_global.914
- __block_literal_global.916
- __block_literal_global.919
- __block_literal_global.931
- __block_literal_global.933
- __serviceLDCMMitigationStatusChanged_block_invoke.912
- __serviceLDCMMitigationStatusChanged_block_invoke.912.cold.1
- __serviceLDCMMitigationStatusChanged_block_invoke.912.cold.2
- __serviceLDCMMitigationStatusChanged_block_invoke.912.cold.3
- __serviceLDCMMitigationStatusChanged_block_invoke.912.cold.4
CStrings:
+ "!*#"
+ "%s: Could not find service with associated port"
+ "%s: IOAccMgrAllowFeatures 0x%x fail kernStatus:%02X"
+ "%s: IOAccMgrRevokeFeatures 0x%x fail kernStatus:%02X"
+ "%s: IOServiceOpen fail kernStatus:%02X, ioConnForService:%04X ioService:%d"
+ "<%@: %p, header: %@, message: %@, numButtons: %lu, numOptions: %lu, visible: %s>"
+ "<%@: %p, title: %@, selected: %d>"
+ "B28@0:8@16B24"
+ "CFUserNotification already exists, ignoring..."
+ "CFUserNotificationCancel() returned error (1st): %d!"
+ "CFUserNotificationCancel() returned error (2nd): %d!"
+ "CFUserNotificationCreate() failed! (error: %d)"
+ "CFUserNotificationUpdate() returned error: %d!"
+ "CN"
+ "Cancelling CFUserNotification..."
+ "Could not add button - maximum of 3 buttons allowed!"
+ "Could not add option - maximum of 8 options allowed!"
+ "Could not dismiss user notification!"
+ "Could not find userNotification! (userNotificationCF: %@)"
+ "Creating CFUserNotification..."
+ "Detected change in Regulatory Domain"
+ "Error encoding extension items! (error: %@)"
+ "IOUserNotification"
+ "IOUserNotificationButton"
+ "IOUserNotificationErrorDomain"
+ "IOUserNotificationOption"
+ "No current location estimates, using last known location estimates"
+ "No last known location estimates"
+ "RegulatoryDomain framework not available..."
+ "T@\"NSArray\",C,N,V_extensionItems"
+ "T@\"NSDictionary\",C,N,V_additionalConfiguration"
+ "T@\"NSLock\",R,N"
+ "T@\"NSMapTable\",R,N"
+ "T@\"NSMutableArray\",&,N,V_buttonsMutable"
+ "T@\"NSMutableArray\",&,N,V_optionsMutable"
+ "T@\"NSNumber\",C,N,V_systemSoundID"
+ "T@\"NSString\",C,N,V_extensionIdentifier"
+ "T@\"NSString\",C,N,V_header"
+ "T@\"NSString\",C,N,V_lockScreenHeader"
+ "T@?,C,N,V_responseHandler"
+ "TB,N,GisVisible,V_visible"
+ "TB,N,V_noDefaultButton"
+ "TB,N,V_notificationCancelled"
+ "TB,N,V_notificationDismissed"
+ "TB,N,V_responseReceived"
+ "TB,N,V_selected"
+ "TB,N,V_shouldAllowLockScreenDismissal"
+ "TB,N,V_shouldDismissOnLock"
+ "TB,N,V_shouldDismissOnUnlock"
+ "TB,N,V_shouldDisplayOnTop"
+ "TB,N,V_shouldHideOnMirroredDisplay"
+ "TB,N,V_shouldIgnoreQuietMode"
+ "TB,N,V_shouldPresentViaSystemAperture"
+ "TB,N,V_useRadioOptions"
+ "TQ,N,V_notificationLevel"
+ "TQ,N,V_response"
+ "TQ,N,V_updateCount"
+ "Updating CFUserNotification..."
+ "^{__CFUserNotification=}24@0:8@16"
+ "_addButton:"
+ "_addOption:"
+ "_additionalConfiguration"
+ "_buttonsMutable"
+ "_checkFor128KHzRestriction"
+ "_extensionIdentifier"
+ "_extensionItems"
+ "_findCFUserNotificationForUserNotification:"
+ "_header"
+ "_lockScreenHeader"
+ "_noDefaultButton"
+ "_notificationCancelled"
+ "_notificationDismissed"
+ "_notificationLevel"
+ "_notificationMapTable"
+ "_notificationMapTableLock"
+ "_optionsMutable"
+ "_response"
+ "_responseHandler"
+ "_responseReceived"
+ "_selected"
+ "_shouldAllowLockScreenDismissal"
+ "_shouldDismissOnLock"
+ "_shouldDismissOnUnlock"
+ "_shouldDisplayOnTop"
+ "_shouldHideOnMirroredDisplay"
+ "_shouldIgnoreQuietMode"
+ "_shouldPresentViaSystemAperture"
+ "_updateCount"
+ "_useRadioOptions"
+ "_userNotificationCallback fired!"
+ "_userNotificationDictionary"
+ "_userNotificationOptionFlags"
+ "_visible"
+ "addButtonWithTitle:"
+ "addEntriesFromDictionary:"
+ "addOptionWithTitle:selected:"
+ "additionalConfiguration"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "buttonWithTitle:"
+ "buttons"
+ "buttonsMutable"
+ "countryCode"
+ "currentEstimates"
+ "dismissNotification"
+ "enumerateObjectsUsingBlock:"
+ "extensionIdentifier"
+ "extensionItems"
+ "header"
+ "initWithHeader:andMessage:"
+ "initWithTitle:"
+ "initWithTitle:selected:"
+ "isVisible"
+ "lastKnownEstimates"
+ "lockScreenHeader"
+ "noDefaultButton"
+ "notificationCancelled"
+ "notificationDismissed"
+ "notificationLevel"
+ "notificationWithHeader:andMessage:"
+ "optionWithTitle:selected:"
+ "options"
+ "optionsMutable"
+ "pointerValue"
+ "presentNotification"
+ "presentNotificationWithResponseHandler:"
+ "response"
+ "responseHandler"
+ "responseReceived"
+ "selected"
+ "setAdditionalConfiguration:"
+ "setButtonsMutable:"
+ "setExtensionIdentifier:"
+ "setExtensionItems:"
+ "setHeader:"
+ "setLockScreenHeader:"
+ "setNoDefaultButton:"
+ "setNotificationCancelled:"
+ "setNotificationDismissed:"
+ "setNotificationLevel:"
+ "setOptionsMutable:"
+ "setResponse:"
+ "setResponseHandler:"
+ "setResponseReceived:"
+ "setSelected:"
+ "setShouldAllowLockScreenDismissal:"
+ "setShouldDismissOnLock:"
+ "setShouldDismissOnUnlock:"
+ "setShouldDisplayOnTop:"
+ "setShouldHideOnMirroredDisplay:"
+ "setShouldIgnoreQuietMode:"
+ "setShouldPresentViaSystemAperture:"
+ "setUpdateCount:"
+ "setUseRadioOptions:"
+ "setVisible:"
+ "shouldAllowLockScreenDismissal"
+ "shouldDismissOnLock"
+ "shouldDismissOnUnlock"
+ "shouldDisplayOnTop"
+ "shouldHideOnMirroredDisplay"
+ "shouldIgnoreQuietMode"
+ "shouldPresentViaSystemAperture"
+ "updateCount"
+ "updateNotification"
+ "useRadioOptions"
+ "v32@?0@\"IOUserNotificationOption\"8Q16^B24"
+ "valueWithPointer:"
+ "visible"

```
