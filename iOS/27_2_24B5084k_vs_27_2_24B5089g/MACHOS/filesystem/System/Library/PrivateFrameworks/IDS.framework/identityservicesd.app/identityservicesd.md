## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-2003.200.33.2.5
-  __TEXT.__text: 0xac72c0
+2003.200.44.0.0
+  __TEXT.__text: 0xac983c
   __TEXT.__auth_stubs: 0x7a10
-  __TEXT.__objc_stubs: 0x4ad40
-  __TEXT.__objc_methlist: 0x2cb54
+  __TEXT.__objc_stubs: 0x4aec0
+  __TEXT.__objc_methlist: 0x2cc1c
   __TEXT.__const: 0x6f528
-  __TEXT.__gcc_except_tab: 0x24b24
-  __TEXT.__objc_methname: 0x7d405
-  __TEXT.__cstring: 0x5b3f9
-  __TEXT.__oslogstring: 0x8add3
+  __TEXT.__gcc_except_tab: 0x24c98
+  __TEXT.__objc_methname: 0x7d6a5
+  __TEXT.__cstring: 0x5b799
+  __TEXT.__oslogstring: 0x8b303
   __TEXT.__objc_classname: 0x8c08
-  __TEXT.__objc_methtype: 0x14509
+  __TEXT.__objc_methtype: 0x14569
   __TEXT.__dlopen_cstrs: 0x148
   __TEXT.__ustring: 0xca0
   __TEXT.__swift5_typeref: 0xa5d6
-  __TEXT.__swift5_reflstr: 0x95a4
+  __TEXT.__swift5_reflstr: 0x95d4
   __TEXT.__swift5_assocty: 0x1ac8
-  __TEXT.__constg_swiftt: 0x85dc
-  __TEXT.__swift5_fieldmd: 0x9ed4
+  __TEXT.__constg_swiftt: 0x85f4
+  __TEXT.__swift5_fieldmd: 0x9ee0
   __TEXT.__swift5_proto: 0x106c
   __TEXT.__swift5_types: 0x9a0
   __TEXT.__swift5_capture: 0x22e0

   __TEXT.__swift_as_ret: 0x39c
   __TEXT.__swift_as_cont: 0x5a4
   __TEXT.__swift5_acfuncs: 0xf0
-  __TEXT.__unwind_info: 0x1fb88
+  __TEXT.__unwind_info: 0x1fc60
   __TEXT.__eh_frame: 0x13a14
-  __DATA_CONST.__const: 0x31758
-  __DATA_CONST.__cfstring: 0x378e0
+  __DATA_CONST.__const: 0x31788
+  __DATA_CONST.__cfstring: 0x37a80
   __DATA_CONST.__objc_classlist: 0x1530
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x840
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0xc08
-  __DATA_CONST.__objc_intobj: 0x2358
+  __DATA_CONST.__objc_intobj: 0x2370
   __DATA_CONST.__objc_arraydata: 0x888
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x3d18
-  __DATA_CONST.__got: 0x46c8
+  __DATA_CONST.__got: 0x46e0
   __DATA_CONST.__auth_ptr: 0x1058
-  __DATA.__objc_const: 0x536d8
-  __DATA.__objc_selrefs: 0x17278
+  __DATA.__objc_const: 0x53720
+  __DATA.__objc_selrefs: 0x172f0
   __DATA.__objc_ivar: 0x3570
-  __DATA.__objc_data: 0xfd68
+  __DATA.__objc_data: 0xfd88
   __DATA.__data: 0x172d0
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0xe08
+  __DATA.__common: 0xe10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 32884
-  Symbols:   2980
-  CStrings:  33467
+  Functions: 32916
+  Symbols:   2983
+  CStrings:  33508
 
Symbols:
+ _kIDSOffGridEntitlement
+ _kIDSPairedDeviceManagerEntitlement
+ _kIDSPinnedIdentityEntitlement
CStrings:
+ "<%@> got kClientChannelMetadataType_SupportsLinkDraining %@"
+ "<%@> link:%@ didCancelDrainOfUnderlyingLinkID:%d linkUUID:%@"
+ "<%@> link:%@ willDisconnectUnderlyingLinkID:%d linkUUID:%@, reason: %d"
+ "<%@> need a client channel to send the event kClientChannelMetadataType_LinkDrainCancelled"
+ "<%@> need a client channel to send the event kClientChannelMetadataType_LinkDraining"
+ "AND is_donated = ? LIMIT 1;"
+ "Caller is neither a platform binary nor entitled {entitlement: %{public}@, signingID: %{public}@, connection: %@}"
+ "Failing creation of IDSDXPCOffGridMessenger collaborator {connection: %@}"
+ "Failing creation of IDSDXPCOffGridStateManager collaborator {connection: %@}"
+ "Failing creation of IDSDXPCPairedDeviceManager collaborator {connection: %@}"
+ "Firewall admitting %@ on service %@ because the sender is in the family circle"
+ "FirewallAllowsFamilyCircle"
+ "FirewallMultiCategory"
+ "LIMIT 1;"
+ "Missing pinned identity entitlement and not a platform binary -- failing creation of IDSDXPCPinnedIdentity collaborator {connection: %@}"
+ "Replaying stored messages for categories %@ after donation into category %u"
+ "SELECT COUNT(1) FROM firewall_record WHERE handle = ? AND category "
+ "SELECT COUNT(1) FROM firewall_record WHERE merge_id = ? AND category "
+ "TB,N,VclientSupportsLinkDraining"
+ "_categoriesFromMask:"
+ "_firewallCategoriesToCheckForService:"
+ "_firewallFamilyCircleAllowsFromURI:service:"
+ "_isFirewallAllowsFamilyCircleEnabled"
+ "_isFirewallMultiCategoryEnabled"
+ "auditToken"
+ "clientSupportsLinkDraining"
+ "controlCategoriesAffectedByDonationInCategory:"
+ "didCancelDrainOfUnderlyingLinkID - alternateDelegate:%@, linkID:%d, linkUUID:%@"
+ "enforcedControlCategories"
+ "got control message: SuspendOTRNegotiationData, too short (%luB)."
+ "isAllowed:inAnyOfCategories:"
+ "isAllowed:inAnyOfCategories:isDonated:"
+ "kClientChannelMetadataType_SupportsLinkDraining should be %d byte, not %u bytes, field: %u"
+ "link:didCancelDrainOfUnderlyingLinkID:linkUUID:"
+ "link:underlyingConnectionDidFailWithLocalAddress:remoteAddress:errorCode:"
+ "link:willDisconnectUnderlyingLinkID:linkUUID:reason:"
+ "setClientSupportsLinkDraining:"
+ "v36@0:8@16c24@\"NSUUID\"28"
+ "v36@0:8@16c24@28"
+ "v44@0:8@16r^{sockaddr=CC[14c]}24r^{sockaddr=CC[14c]}32i40"
+ "willDisconnectUnderlyingLinkID - alternateDelegate:%@, linkID:%d, linkUUID:%@, reason: %d"
```
