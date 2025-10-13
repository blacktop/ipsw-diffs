## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-985.20.0.0.0
-  __TEXT.__text: 0x1ab030
+985.22.0.0.0
+  __TEXT.__text: 0x1abdd8
   __TEXT.__auth_stubs: 0x1ad0
-  __TEXT.__objc_methlist: 0x10534
+  __TEXT.__objc_methlist: 0x10554
   __TEXT.__const: 0x2ca8
   __TEXT.__dlopen_cstrs: 0x966
   __TEXT.__swift5_typeref: 0x7e5

   __TEXT.__swift5_fieldmd: 0x6a0
   __TEXT.__swift5_proto: 0x270
   __TEXT.__swift5_types: 0xac
-  __TEXT.__cstring: 0x1de61
-  __TEXT.__gcc_except_tab: 0x7820
-  __TEXT.__oslogstring: 0x1ab6b
+  __TEXT.__cstring: 0x1de80
+  __TEXT.__gcc_except_tab: 0x7898
+  __TEXT.__oslogstring: 0x1adb0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x54a8
+  __TEXT.__unwind_info: 0x54d8
   __TEXT.__eh_frame: 0x570
   __TEXT.__objc_classname: 0xfb4
-  __TEXT.__objc_methname: 0x26c9e
+  __TEXT.__objc_methname: 0x26d9a
   __TEXT.__objc_methtype: 0x382b
-  __TEXT.__objc_stubs: 0x1bd60
+  __TEXT.__objc_stubs: 0x1bdc0
   __DATA_CONST.__got: 0x910
   __DATA_CONST.__const: 0x5018
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8188
+  __DATA_CONST.__objc_selrefs: 0x81a0
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x19f8
   __AUTH_CONST.__auth_got: 0xd78
   __AUTH_CONST.__const: 0x32d0
   __AUTH_CONST.__cfstring: 0x18140
-  __AUTH_CONST.__objc_const: 0x15620
+  __AUTH_CONST.__objc_const: 0x15640
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_intobj: 0x37f8
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0xe58
   __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x1228
+  __DATA.__objc_ivar: 0x122c
   __DATA.__data: 0x1700
   __DATA.__bss: 0x4fa0
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6EFD48C0-D50A-3317-A84C-34C21DD960A4
-  Functions: 7465
+  UUID: 9B06B3D7-D950-352C-B4A5-27D0B619E53E
+  Functions: 7469
   Symbols:   1080
-  CStrings:  14933
+  CStrings:  14943
 
CStrings:
+ "WiFiCredentialSharing_TESTABLE"
+ "[corewifi] %{public}s (%{public}s:%u) [nearbysync] Failed to send %{public}@ to nearby device (%{public}@ less than %lu seconds ago"
+ "[corewifi] %{public}s (%{public}s:%u) [nearbysync] Failed to share network with nearby device (%{public}@ less than %lu seconds ago"
+ "[corewifi] [nearbysync] Failed to send %{public}@ to nearby device (%{public}@) after %d retries"
+ "[corewifi] [wifi-network-sharing] Applying 'testable' ask-to-share (from appex) request rate limit (%lu)"
+ "[corewifi] [wifi-network-sharing] Applying 'testable' authorization request rate limit (%lu)"
+ "[corewifi] [wifi-network-sharing] Exceeded ask-to-share (from appex) request rate limit (clientID=%{public}@, networkID=%{public}@)"
+ "__descriptorForRateLimitAskToShareFromAppexRequestWithClientID:networkID:"
+ "__failedNearbyNetworkSyncRequestTimestampForDevice:network:"
+ "__shouldRateLimitAskToShareFromAppexRequestWithClientID:networkID:"
+ "__updateFailedNearbyNetworkSyncRequestTimestampForDevice:network:"
+ "__updateRateLimitAskToShareFromAppexRequestTimestampCacheForClientID:networkID:"
+ "_failedNearbySyncRequestHistory"
- "[corewifi] [wifi-network-sharing] Exceeded ask-to-share (from appex) request rate limit (clientID=%{public}@)"
- "__shouldRateLimitAskToShareFromAppexRequestWithClientID:"
- "__updateRateLimitAskToShareFromAppexRequestTimestampCacheForClientID:"

```
