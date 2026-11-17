## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-42.4.1.0.0
-  __TEXT.__text: 0x253e40
+42.6.0.0.0
+  __TEXT.__text: 0x258740
   __TEXT.__auth_stubs: 0x3c80
-  __TEXT.__objc_stubs: 0x1f8c0
-  __TEXT.__objc_methlist: 0xec2c
-  __TEXT.__const: 0x4d70
+  __TEXT.__objc_stubs: 0x1f980
+  __TEXT.__objc_methlist: 0xec54
+  __TEXT.__const: 0x4d60
   __TEXT.__gcc_except_tab: 0x5a7c
-  __TEXT.__cstring: 0x59c53
+  __TEXT.__cstring: 0x5a123
   __TEXT.__objc_classname: 0x11a3
-  __TEXT.__objc_methname: 0x2db75
-  __TEXT.__objc_methtype: 0x43a9
+  __TEXT.__objc_methname: 0x2dc05
+  __TEXT.__objc_methtype: 0x43b9
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x9efa
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x1f00
-  __TEXT.__constg_swiftt: 0x2110
-  __TEXT.__swift5_reflstr: 0x1bab
-  __TEXT.__swift5_fieldmd: 0x19a8
+  __TEXT.__swift5_typeref: 0x1f24
+  __TEXT.__constg_swiftt: 0x2138
+  __TEXT.__swift5_reflstr: 0x1bdb
+  __TEXT.__swift5_fieldmd: 0x19b4
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_capture: 0x1fbc

   __TEXT.__swift_as_cont: 0xe8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x98d0
-  __TEXT.__eh_frame: 0x2db8
-  __DATA_CONST.__const: 0xcf58
+  __TEXT.__unwind_info: 0x9978
+  __TEXT.__eh_frame: 0x3008
+  __DATA_CONST.__const: 0xcf80
   __DATA_CONST.__cfstring: 0xbb40
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__auth_got: 0x1e50
-  __DATA_CONST.__got: 0x1170
+  __DATA_CONST.__got: 0x1178
   __DATA_CONST.__auth_ptr: 0x7c0
-  __DATA.__objc_const: 0x20800
-  __DATA.__objc_selrefs: 0x94a8
-  __DATA.__objc_ivar: 0x18ec
+  __DATA.__objc_const: 0x20840
+  __DATA.__objc_selrefs: 0x94d8
+  __DATA.__objc_ivar: 0x18f0
   __DATA.__objc_data: 0x3728
-  __DATA.__data: 0x5a30
-  __DATA.__common: 0x3a8
+  __DATA.__data: 0x5a80
+  __DATA.__common: 0x3a0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libAccessibility.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12180
-  Symbols:   1710
-  CStrings:  16525
+  Functions: 12215
+  Symbols:   1711
+  CStrings:  16553
 
Symbols:
+ _OBJC_CLASS_$_STMediaStatusDomain
CStrings:
+ "-[AAConversationDetectSessionManager _deregisterFromMediaStatusChanges]"
+ "-[AAConversationDetectSessionManager _mediaStatusDomainDataChanged:]"
+ "-[AAConversationDetectSessionManager _registerForMediaStatusChanges]"
+ "@\"STMediaStatusDomain\""
+ "CD Session activate skipped, session already active"
+ "Clearing incomingPairedDevices (%@): %@"
+ "Deregistering for STMediaStatusDomainData changes"
+ "IncomingPairedDevices"
+ "Loaded %d incomingPairedDevices from prefs: %@"
+ "Microphone in-use state changed: %s -> %s, audioRecordingAttributions count %d"
+ "No cloudMetadata (record not yet saved to cloud) -- creating new %@ record"
+ "Pruned incomingPairedDevices without a MagicSettings record or legacy blob entry: %@"
+ "Registering for STMediaStatusDomainData changes, domain valid: %s"
+ "Removed %@ from incomingPairedDevices (removed from legacyMagicPairingSettingsRecords blob)"
+ "Removed %@ from incomingPairedDevices (unpaired)"
+ "Updated pause conversation state to: %s, isWirelessSplitterOn: %s, isSpeechDetectionStyleDisallowed: %s, isMicrophoneInUse: %s"
+ "_deregisterFromMediaStatusChanges"
+ "_incomingPairedDevices"
+ "_mediaStatusDomain"
+ "_mediaStatusDomainDataChanged:"
+ "_registerForMediaStatusChanges"
+ "audioRecordingAttributions"
+ "bluetooth device info zone purged"
+ "cloudMetadata failed to unarchive -- creating new %@ record"
+ "incomingPairedDevices call failed because device is in beforeFirstUnlock state"
+ "incomingPairedDevices update dropped because device is in beforeFirstUnlock state"
+ "incomingPairedDevicesPrefs"
+ "local records reset"
+ "observeDataWithBlock:"
+ "stringArrayForKey:"
+ "v16@?0@\"STMediaStatusDomainData\"8"
- "Failed to unarchive record -- creating new %@ record"
- "Updated pause conversation state to: %s, isWirelessSplitterOn: %s, isSpeechDetectionStyleDisallowed: %s"
- "incomingPairedDevices"
```
