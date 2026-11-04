## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

```diff

-446.0.4.0.0
-  __TEXT.__text: 0xd8e4
-  __TEXT.__objc_methlist: 0xdb8
+447.0.1.0.0
+  __TEXT.__text: 0xe23c
+  __TEXT.__objc_methlist: 0xe38
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x16ed
+  __TEXT.__cstring: 0x1762
   __TEXT.__oslogstring: 0xa7b
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__unwind_info: 0x518
+  __TEXT.__unwind_info: 0x548
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x468
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f8
+  __DATA_CONST.__objc_selrefs: 0x838
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x1bb0
+  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__objc_const: 0x1c80
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xf8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x130
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x50

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 366
-  Symbols:   687
-  CStrings:  213
+  Functions: 379
+  Symbols:   709
+  CStrings:  215
 
Symbols:
+ +[THNearbyNetworkCredentials supportsSecureCoding]
+ -[THClient handleActiveNearbyNetworksResponse:preferredNetworkRecord:error:apiName:isInternal:nearbyType:completion:]
+ -[THClient retrieveNearbyNetworkCredentialsInternallyWithCompletion:]
+ -[THClient retrieveNearbyNetworkCredentialsWithCompletion:]
+ -[THNearbyNetworkCredentials encodeWithCoder:]
+ -[THNearbyNetworkCredentials initThreadCredentials:extendedPANID:borderAgentID:activeOperationalDataSet:PSKC:networkKey:channel:panID:creationDate:lastModificationDate:isPreferredNetworkCredentials:]
+ -[THNearbyNetworkCredentials initThreadCredentials:isPreferredNetworkCredentials:]
+ -[THNearbyNetworkCredentials initWithActiveDataSetRecord:isPreferredNetworkCredentials:]
+ -[THNearbyNetworkCredentials initWithCoder:]
+ -[THNearbyNetworkCredentials isPreferredNetworkCredentials]
+ _OBJC_CLASS_$_THNearbyNetworkCredentials
+ _OBJC_IVAR_$_THNearbyNetworkCredentials._isPreferredNetworkCredentials
+ _OBJC_METACLASS_$_THNearbyNetworkCredentials
+ __OBJC_$_CLASS_METHODS_THNearbyNetworkCredentials
+ __OBJC_$_INSTANCE_METHODS_THNearbyNetworkCredentials
+ __OBJC_$_INSTANCE_VARIABLES_THNearbyNetworkCredentials
+ __OBJC_$_PROP_LIST_THNearbyNetworkCredentials
+ __OBJC_CLASS_RO_$_THNearbyNetworkCredentials
+ __OBJC_METACLASS_RO_$_THNearbyNetworkCredentials
+ ___59-[THClient retrieveNearbyNetworkCredentialsWithCompletion:]_block_invoke
+ ___59-[THClient retrieveNearbyNetworkCredentialsWithCompletion:]_block_invoke_2
+ ___69-[THClient retrieveNearbyNetworkCredentialsInternallyWithCompletion:]_block_invoke
+ ___69-[THClient retrieveNearbyNetworkCredentialsInternallyWithCompletion:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e77_v32?0"NSSet"8"THThreadNetworkCredentialsActiveDataSetRecord"16"NSError"24ls32l8s40l8
+ _objc_retainBlock
- -[THClient handleActiveNearbyNetworksResponse:error:isInternal:completion:]
- ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16ls32l8s40l8
- _objc_release_x1
CStrings:
+ "THNearbyNetworkCredentials.isPreferred"
+ "v32@?0@\"NSSet\"8@\"THThreadNetworkCredentialsActiveDataSetRecord\"16@\"NSError\"24"
```
