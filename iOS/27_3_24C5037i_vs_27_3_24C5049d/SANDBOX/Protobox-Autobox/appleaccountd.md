## appleaccountd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
 	)
 )
 

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		28
 		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
```
