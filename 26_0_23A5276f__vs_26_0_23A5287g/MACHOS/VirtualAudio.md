## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1364.102.2.1.0
-  __TEXT.__text: 0x4f2380
-  __TEXT.__auth_stubs: 0x26d0
-  __TEXT.__objc_stubs: 0xa00
-  __TEXT.__init_offsets: 0x4d4
-  __TEXT.__objc_methlist: 0x134
-  __TEXT.__const: 0xb0ada
-  __TEXT.__gcc_except_tab: 0x5c3f0
-  __TEXT.__cstring: 0x284ca
+1364.110.0.0.0
+  __TEXT.__text: 0x4fa19c
+  __TEXT.__auth_stubs: 0x26e0
+  __TEXT.__objc_stubs: 0x9e0
+  __TEXT.__init_offsets: 0x4d8
+  __TEXT.__objc_methlist: 0x124
+  __TEXT.__const: 0xb0afa
+  __TEXT.__gcc_except_tab: 0x5cb68
+  __TEXT.__cstring: 0x285f6
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
-  __TEXT.__swift5_capture: 0x158
-  __TEXT.__oslogstring: 0x4d60a
-  __TEXT.__objc_methname: 0x723
+  __TEXT.__swift5_capture: 0x178
+  __TEXT.__oslogstring: 0x4dc66
+  __TEXT.__objc_methname: 0x710
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c
   __TEXT.__swift5_fieldmd: 0x68

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x28
-  __TEXT.__objc_methtype: 0x199
+  __TEXT.__objc_methtype: 0x23b
   __TEXT.__dof_VirtualAu: 0x340
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0x10c28
-  __TEXT.__eh_frame: 0x778
-  __DATA_CONST.__auth_got: 0x1380
+  __TEXT.__unwind_info: 0x11098
+  __TEXT.__eh_frame: 0x7a0
+  __DATA_CONST.__auth_got: 0x1388
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x26b28
-  __DATA_CONST.__cfstring: 0x2d60
+  __DATA_CONST.__const: 0x27678
+  __DATA_CONST.__cfstring: 0x2de0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x398
-  __DATA.__objc_selrefs: 0x2b8
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_const: 0x378
+  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x268
   __DATA.__data: 0x340
-  __DATA.__bss: 0x237a0
+  __DATA.__bss: 0x242d0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 56E065AD-0855-379C-AFE3-AA6B68732CB0
-  Functions: 11059
+  UUID: A1F6CE5C-A924-39FB-B524-ABA20B7AC4E5
+  Functions: 11351
   Symbols:   772
-  CStrings:  11204
+  CStrings:  11243
 
CStrings:
+ "%25s:%-5d - Clearing User Preferred Ports."
+ "%25s:%-5d ASSERTION FAILURE: \"HP_Object with ID %u at address %p is being destroyed by something other than the HP_ObjectDestroyer\""
+ "%25s:%-5d ASSERTION FAILURE: \"VirtualAudio_DevicePropertyManager has not been initialized.\""
+ "%25s:%-5d Active ports for route configuration (%s), user preferred input: (%s) returned: %s"
+ "%25s:%-5d CAException thrown during stream destruction: '%s'."
+ "%25s:%-5d Calling dtor for: %u"
+ "%25s:%-5d Could not retrieve device name for localized Microphone Port"
+ "%25s:%-5d Destroying HP object with ID %lu at address %p."
+ "%25s:%-5d Device has Apple Display UID"
+ "%25s:%-5d Device has Apple Display VID_PID"
+ "%25s:%-5d Found mix-match Studio Display attempt - Disallowing"
+ "%25s:%-5d HP_Object at ID %lu is invalid."
+ "%25s:%-5d Ignoring an attempt to set un-owned port routability for port with name \"%s\", UID \"%s\", and type '%s'"
+ "%25s:%-5d No session object found: session id = %u"
+ "%25s:%-5d Not registered with ADAM as headphones"
+ "%25s:%-5d PropertyCache has expired, ignoring property changed notification."
+ "%25s:%-5d Routable BT ports found, clearing user preferred input %s"
+ "%25s:%-5d SetHapticVibrationParameterOnDSP vibrating = %d"
+ "%25s:%-5d Setting bypass of %s to %u: %u"
+ "%25s:%-5d Siblings for port %s : %zd"
+ "%25s:%-5d Standard Library exception thrown during stream destruction: %s."
+ "%25s:%-5d The initial magnetic coex mitigation requirement was set to %s for LTEBand40, %s for LTEBand41, %s for LTEBand42, %s for LTEBand48"
+ "%25s:%-5d The magnetic coex mitigation requirement was set to %s for LTEBand40, %s for LTEBand41, %s for LTEBand42, %s for LTEBand48"
+ "%25s:%-5d Unable to unlock VirtualAudio_DevicePropertyManager cache mutex."
+ "%25s:%-5d Unknown exception thrown during stream destruction."
+ "%25s:%-5d Unsupported RoutingUtilities::Result"
+ "%25s:%-5d Updating user preferred input usage: Not a VP route. returning early"
+ "%25s:%-5d User preferred port in route config: %s"
+ "%25s:%-5d VirtualAudio_DevicePropertyManager has expired. Ignoring property changed notifications."
+ "%25s:%-5d setting bypass of %s to %u: %u"
+ "@@ Strips Jun 28 2025 20:14:58"
+ "Apple Display input required for this route"
+ "Apple Display output disallowed for this route"
+ "Apple Display output required for this route"
+ "Destroying HP_Objects with IDs: "
+ "LTEBand40"
+ "LTEBand40Enabled"
+ "LTEBand41"
+ "LTEBand41Enabled"
+ "LTEBand42"
+ "LTEBand42Enabled"
+ "LTEBand48"
+ "LTEBand48Enabled"
+ "RoutingManager_Utilities.h"
+ "device-name"
+ "getInitialRFFlags"
+ "initialRFFlags"
+ "kCategoryNotSupported"
+ "kOk"
+ "kRouteProcessed"
+ "kRoutingNotSupported"
+ "{RFMitigationFlags=\"mitigateNRBand41\"B\"mitigateNRBand7x\"B\"mitigateLTEBand40\"B\"mitigateLTEBand41\"B\"mitigateLTEBand42\"B\"mitigateLTEBand48\"B}"
+ "{RFMitigationFlags=BBBBBB}16@0:8"
- "%25s:%-5d ASSERTION FAILURE: \"The VirtualAudio_Port with ID %u at address %p is being destroyed by something other than the HP_Object Destruction Handler\""
- "%25s:%-5d Could not retrieve localized device name"
- "%25s:%-5d Destroying HP object at address %p."
- "%25s:%-5d Device is Apple Display"
- "%25s:%-5d Property not supported: %s"
- "%25s:%-5d Result of setting bypass of %s to %u: %u"
- "%25s:%-5d qqq SetHapticVibrationParameterOnDSP vibrating = %d"
- "@@ Strips Jun 18 2025 21:04:33"
- "AUControlFreak"
- "AUVolumeTaper"
- "B"
- "B16@0:8"
- "Destroying PlugIn objects: "
- "device-name-localized"
- "isNr41Enabled"
- "isNr7xEnabled"
- "nr41Enabled"
- "nr7xEnabled"

```
