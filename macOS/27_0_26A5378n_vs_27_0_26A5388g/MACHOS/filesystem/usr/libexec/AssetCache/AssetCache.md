## AssetCache

> `/usr/libexec/AssetCache/AssetCache`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__objc_methtype`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-264.0.0.0.0
-  __TEXT.__text: 0x1eabe4
+265.0.0.0.0
+  __TEXT.__text: 0x1e49b0
   __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_stubs: 0xfbc0
-  __TEXT.__objc_methlist: 0x6b14
+  __TEXT.__objc_stubs: 0xfce0
+  __TEXT.__objc_methlist: 0x6b24
   __TEXT.__cstring: 0x8737
-  __TEXT.__const: 0x3ad70
+  __TEXT.__const: 0x3ade0
   __TEXT.__gcc_except_tab: 0x2a88
-  __TEXT.__objc_methname: 0x1275d
-  __TEXT.__oslogstring: 0x7cc8
+  __TEXT.__objc_methname: 0x127d5
+  __TEXT.__oslogstring: 0x7f1d
   __TEXT.__objc_classname: 0x3b6
   __TEXT.__objc_methtype: 0x21b3
   __TEXT.__ustring: 0x19e
-  __TEXT.__unwind_info: 0x1a90
+  __TEXT.__unwind_info: 0x1b10
   __TEXT.__eh_frame: 0xc0
-  __DATA_CONST.__const: 0xb150
+  __DATA_CONST.__const: 0xb2e0
   __DATA_CONST.__cfstring: 0x9120
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x910
   __DATA_CONST.__auth_got: 0x880
-  __DATA_CONST.__got: 0x908
+  __DATA_CONST.__got: 0x910
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0xcaf0
-  __DATA.__objc_selrefs: 0x4348
+  __DATA.__objc_selrefs: 0x4390
   __DATA.__objc_ivar: 0xaa0
   __DATA.__objc_data: 0xc30
-  __DATA.__data: 0xbf8
-  __DATA.__common: 0xab0
+  __DATA.__data: 0xd18
+  __DATA.__common: 0xab8
   __DATA.__bss: 0x128
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3445
-  Symbols:   578
-  CStrings:  5697
+  Functions: 3465
+  Symbols:   579
+  CStrings:  5710
 
Symbols:
+ _OBJC_CLASS_$_NSURLComponents
CStrings:
+ "#%@ %@%@: Failed to decode header: %{public}@"
+ "#%@ %@%@: Failed to verify header: %{private}@"
+ "#%@ %@%@: assetIDForMethod:%@ URL:%{private}@ namespace:%@ index:%@ icloudHeader:%{private}@"
+ "#%@ %@%@: icloudHeaderIsValid:%{private}@"
+ "#%@ %@%@: icloudHeaderIsValid:%{private}@ -> %d"
+ "#%@ %@[%p]%@: %@ing %llu bytes to URL %@ with headers %{private}@"
+ "#%@ %@[%p]%@: Received %@ request%@ %@ %@, headers = %{private}@"
+ "#%@ %@[%p]%@: Received %u response, headers are %{private}@"
+ "#%@ %@[%p]%@: Request headers are %{private}@"
+ "#%@ %@[%p]%@: Request method = %@, headers = %{private}@"
+ "#%@ %@[%p]%@: Response status = %ld, headers = %{private}@"
+ "#%@ %@[%p]%@: Upload response body [%ld] \"%{private}@\""
+ "#%@ %@[%p]%@: Upload response code %d, headers = %{private}@"
+ "#%@ %@[%p]%@: blobFromEntityHeaders:%{private}@"
+ "#%@ %@[%p]%@: import result: wt=%d code=%d headers=%{private}@"
+ "#%@ %{private}@"
+ "#%@ %{public}@"
+ "#%@ Absorb %@ with status %ld, reason code %d, headers %{private}@"
+ "#%@ Cache query from %{private}@ for asset %@"
+ "#%@ Cache query from %{private}@ for asset %@, headers = %{private}@"
+ "#%@ Cache query from peer server %{private}@ denied because %{private}@ is not a friend; see %@ setting"
+ "#%@ Failed to convert peer address %{private}@ to network representation"
+ "#%@ Failed to determine if notification from peer server %{private}@ is from a friend"
+ "#%@ Import request from %{private}@ denied because the server is being tested"
+ "#%@ Notification from peer server %{private}@ is from a friend"
+ "#%@ Peer address %{private}@ is not a friend"
+ "#%@ Query headers = %{private}@"
+ "#%@ Querying peer server %{private}@ returned status %ld, headers = %{private}@"
+ "#%@ Received %@ request from %{private}@"
+ "#%@ Received notification from peer server %{private}@"
+ "#%@ Received notification from peer server %{private}@, headers = %{private}@"
+ "#%@ Request from %{private}@ to %@ %@ denied because %{private}@ is in my %@ setting; check %{private}@'s %@ setting"
+ "#%@ Request from %{private}@ to %@ %@ denied because the server is being tested"
+ "#%@ Request%@ %@ %{private}@ %@ because %@"
+ "#%@ Request%@ %@ %{private}@ denied because the URL is invalid"
+ "#%@ Request%@ %@ %{private}@ denied because the server is too busy; see %@ setting"
+ "#%@ Request%@ %@ %{public}@ denied because the server is suspended pending successful registration"
+ "#%@ Selected parent server %{public}@%@"
+ "#%@ Unable to encode headers: %@; headers=%{private}@"
+ "%@[%p]: Received %u response, headers are %{private}@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECAnalyticsReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECAssetHandler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECAssetRequestor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECAssetUploader.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECCacheManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECCacheReader.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECCacheWriter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECConfig.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECDDMReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECExtent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECManagementMetricsReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECMetricsManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECMetricsUploader.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECNetworkUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECParentManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECPeerManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECPeerNotify.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECPeerQuery.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECRegistrant.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECRemoteServerManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECResponse.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECServer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECStatisticsAggregator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.imMeVc/Sources/EdgeCache/EdgeCache/ECStatisticsReporter.m"
+ "265"
+ "A server with address %{private}@ is not known to this server; see %@ and %@ settings"
+ "Got back public IP %{private}@"
+ "Notify headers = %{private}@"
+ "Notifying peer server %{private}@ returned status %ld, headers = %{private}@"
+ "Request for %@ from %@ failed: HTTP response %u, body \"%{private}@\""
+ "Request for %@ from %@ failed: HTTP response %u, body \"%{private}@\"; retrying with new %@"
+ "This computer's local IP address %{public}@ is neither %@ nor equal to its public IP address %{public}@.  This configuration is not supported."
+ "This server (%{private}@) cannot be its own parent; see %@ setting"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "fragment"
+ "password"
+ "safeURL:"
+ "setFragment:"
+ "setPassword:"
+ "setQuery:"
+ "setUser:"
+ "user"
- "#%@ %@%@: assetIDForMethod:%@ URL:%@ namespace:%@ index:%@ icloudHeader:%@"
- "#%@ %@%@: icloudHeaderIsValid:%@"
- "#%@ %@%@: icloudHeaderIsValid:%@ -> %d"
- "#%@ %@[%p]%@: %@ing %llu bytes to URL %@ with headers %@"
- "#%@ %@[%p]%@: Received %@ request%@ %@ %@, headers = %@"
- "#%@ %@[%p]%@: Received %u response, headers are %@"
- "#%@ %@[%p]%@: Request headers are %@"
- "#%@ %@[%p]%@: Request method = %@, headers = %@"
- "#%@ %@[%p]%@: Response status = %ld, headers = %@"
- "#%@ %@[%p]%@: Upload response body [%ld] \"%@\""
- "#%@ %@[%p]%@: Upload response code %d, headers = %@"
- "#%@ %@[%p]%@: blobFromEntityHeaders:%@"
- "#%@ %@[%p]%@: import result: wt=%d code=%d headers=%@"
- "#%@ Absorb %@ with status %ld, reason code %d, headers %@"
- "#%@ Cache query from %@ for asset %@"
- "#%@ Cache query from %@ for asset %@, headers = %@"
- "#%@ Cache query from peer server %@ denied because %@ is not a friend; see %@ setting"
- "#%@ Failed to convert peer address %@ to network representation"
- "#%@ Failed to determine if notification from peer server %@ is from a friend"
- "#%@ Import request from %@ denied because the server is being tested"
- "#%@ Notification from peer server %@ is from a friend"
- "#%@ Peer address %@ is not a friend"
- "#%@ Query headers = %@"
- "#%@ Querying peer server %@ returned status %ld, headers = %@"
- "#%@ Received %@ request from %@"
- "#%@ Received notification from peer server %@"
- "#%@ Received notification from peer server %@, headers = %@"
- "#%@ Request from %@ to %@ %@ denied because %@ is in my %@ setting; check %@'s %@ setting"
- "#%@ Request from %@ to %@ %@ denied because the server is being tested"
- "#%@ Request%@ %@ %@ %@ because %@"
- "#%@ Request%@ %@ %@ denied because the URL is invalid"
- "#%@ Request%@ %@ %@ denied because the server is suspended pending successful registration"
- "#%@ Request%@ %@ %@ denied because the server is too busy; see %@ setting"
- "#%@ Selected parent server %@%@"
- "#%@ Unable to encode headers: %@; headers=%@"
- "%@[%p]: Received %u response, headers are %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECAnalyticsReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECAssetHandler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECAssetRequestor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECAssetUploader.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECCacheManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECCacheReader.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECCacheWriter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECConfig.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECDDMReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECExtent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECManagementMetricsReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECMetricsManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECMetricsUploader.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECNetworkUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECParentManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECPeerManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECPeerNotify.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECPeerQuery.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECRegistrant.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECRemoteServerManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECResponse.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECServer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECStatisticsAggregator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VdGG9p/Sources/EdgeCache/EdgeCache/ECStatisticsReporter.m"
- "264"
- "A server with address %@ is not known to this server; see %@ and %@ settings"
- "Got back public IP %@"
- "Notify headers = %@"
- "Notifying peer server %@ returned status %ld, headers = %@"
- "Request for %@ from %@ failed: HTTP response %u, body \"%@\""
- "Request for %@ from %@ failed: HTTP response %u, body \"%@\"; retrying with new %@"
- "This computer's local IP address %@ is neither %@ nor equal to its public IP address %@.  This configuration is not supported."
- "This server (%@) cannot be its own parent; see %@ setting"
```
