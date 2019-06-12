"""Generated message classes for gkehub version v1beta1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'gkehub'


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class GkehubProjectsLocationsGetRequest(_messages.Message):
  r"""A GkehubProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class GkehubProjectsLocationsGlobalMembershipsCreateRequest(_messages.Message):
  r"""A GkehubProjectsLocationsGlobalMembershipsCreateRequest object.

  Fields:
    membership: A Membership resource to be passed as the request body.
    membershipId: Client chosen ID for the membership. The ID must be a valid
      RFC 1123 compliant DNS label. In particular, the ID must be:   1. At
      most 63 characters in length   2. It must consist of lower case
      alphanumeric characters or `-`   3. It must start and end with an
      alphanumeric character I.e. ID must match the regex:
      `[a-z0-9]([-a-z0-9]*[a-z0-9])?` with at most 63 characters.
    parent: The parent in whose context the membership is created. The parent
      value is in the format: `projects/[project_id]/locations/global`.
  """

  membership = _messages.MessageField('Membership', 1)
  membershipId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class GkehubProjectsLocationsGlobalMembershipsDeleteRequest(_messages.Message):
  r"""A GkehubProjectsLocationsGlobalMembershipsDeleteRequest object.

  Fields:
    name: The membership resource name in the format:
      `projects/[project_id]/locations/global/memberships/[membership_id]`
  """

  name = _messages.StringField(1, required=True)


class GkehubProjectsLocationsGlobalMembershipsGetRequest(_messages.Message):
  r"""A GkehubProjectsLocationsGlobalMembershipsGetRequest object.

  Fields:
    name: The Membership resource name in the format:
      `projects/[project_id]/locations/global/memberships/[membership_id]`
  """

  name = _messages.StringField(1, required=True)


class GkehubProjectsLocationsGlobalMembershipsListRequest(_messages.Message):
  r"""A GkehubProjectsLocationsGlobalMembershipsListRequest object.

  Fields:
    filter: Lists the Memberships that match the filter expression. A filter
      expression filters the resources listed in the response. The expression
      must be of the form `<field> <operator> <value>` where operators: `<`,
      `>`, `<=`, `>=`, `!=`, `=`, `:` are supported (colon `:` represents a
      HAS operator which is roughly synonymous with equality). <field> can
      refer to a proto or JSON field, or a synthetic field. Field names can be
      camelCase or snake_case.  Examples: - Filter by name:   name = "projects
      /foo-proj/locations/global/membership/bar  - Filter by labels:   -
      Resources that have a key called `foo`     labels.foo:*   - Resources
      that have a key called `foo` whose value is `bar`     labels.foo = bar
      - Filter by state:    - Members in CREATING state.      state = CREATING
    orderBy: Field to use to sort the list.
    pageSize: When requesting a 'page' of resources, `page_size` specifies
      number of resources to return. If unspecified or set to 0, all resources
      will be returned.
    pageToken: Token returned by previous call to `ListMemberships` which
      specifies the position in the list from where to continue listing the
      resources.
    parent: The parent in whose context the memberships are listed. The parent
      value is in the format: `projects/[project_id]/locations/global`.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class GkehubProjectsLocationsGlobalMembershipsPatchRequest(_messages.Message):
  r"""A GkehubProjectsLocationsGlobalMembershipsPatchRequest object.

  Fields:
    membership: A Membership resource to be passed as the request body.
    name: The membership resource name in the format:
      `projects/[project_id]/locations/global/memberships/[membership_id]`
    updateMask: Mask of fields to update. At least one field path must be
      specified in this mask.
  """

  membership = _messages.MessageField('Membership', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class GkehubProjectsLocationsListRequest(_messages.Message):
  r"""A GkehubProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class GkehubProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A GkehubProjectsLocationsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class GkehubProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A GkehubProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class GkehubProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A GkehubProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class GkehubProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A GkehubProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class GoogleRpcStatus(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListMembershipsResponse(_messages.Message):
  r"""Response message for the `GkeHubMembershipService.ListMemberships`
  method.

  Fields:
    nextPageToken: A token to request the next page of resources from the
      `ListMemberships` method. The value of an empty string means that there
      are no more resources to return.
    resources: The list of Memberships contained within the parent.
  """

  nextPageToken = _messages.StringField(1)
  resources = _messages.MessageField('Membership', 2, repeated=True)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Membership(_messages.Message):
  r"""Membership contains information about a member cluster.

  Messages:
    LabelsValue: GCP labels for this membership.

  Fields:
    createTime: Output only. Timestamp for when the Membership was created.
    deleteTime: Output only. Timestamp for when the Membership was deleted.
    description: A required description of this membership, limited to 63
      characters.
    endpoint: A MembershipEndpoint attribute.
    labels: GCP labels for this membership.
    name: Output only. The unique name of this domain resource in the format:
      `projects/[project_id]/locations/global/memberships/[membership_id]`.
      `membership_id` can only be set at creation time using the
      `membership_id` field in the creation request. `membership_id` must be a
      valid RFC 1123 compliant DNS label. In particular, it must be:   1. At
      most 63 characters in length   2. It must consist of lower case
      alphanumeric characters or `-`   3. It must start and end with an
      alphanumeric character I.e. `membership_id` must match the regex:
      `[a-z0-9]([-a-z0-9]*[a-z0-9])?` with at most 63 characters.
    state: Output only. State of the Membership resource.
    updateTime: Output only. Timestamp for when the Membership was last
      updated.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""GCP labels for this membership.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  deleteTime = _messages.StringField(2)
  description = _messages.StringField(3)
  endpoint = _messages.MessageField('MembershipEndpoint', 4)
  labels = _messages.MessageField('LabelsValue', 5)
  name = _messages.StringField(6)
  state = _messages.MessageField('MembershipState', 7)
  updateTime = _messages.StringField(8)


class MembershipEndpoint(_messages.Message):
  r"""MembershipEndpoint contains the information to reach a member.

  Fields:
    gcpResourceLink: If this API server is also a Google service provide the
      self link of its GCP resource. For example, the FQDN to a GKE Cluster
      that backs this Membership:
      https://container.googleapis.com/v1/projects/x/zones/us-
      west1-a/clusters/c0 It can be at the most 1000 characters in length.
    oidcConfig: OIDC configuration to use to authenticate users against with
      this member.
  """

  gcpResourceLink = _messages.StringField(1)
  oidcConfig = _messages.MessageField('OidcConfig', 2)


class MembershipState(_messages.Message):
  r"""State of the Membership resource.

  Enums:
    CodeValueValuesEnum: Code indicating the state of the Membership resource.

  Fields:
    code: Code indicating the state of the Membership resource.
    description: Human readable description of the issue.
    updateTime: The last update time of this state by the controllers
  """

  class CodeValueValuesEnum(_messages.Enum):
    r"""Code indicating the state of the Membership resource.

    Values:
      CODE_UNSPECIFIED: Not set.
      CREATING: CREATING indicates the cluster is being registered.
      READY: READY indicates the cluster is registered.
      DELETING: DELETING indicates that the cluster is being unregistered.
      UPDATING: UPDATING indicates that the cluster registration is being
        updated.
    """
    CODE_UNSPECIFIED = 0
    CREATING = 1
    READY = 2
    DELETING = 3
    UPDATING = 4

  code = _messages.EnumField('CodeValueValuesEnum', 1)
  description = _messages.StringField(2)
  updateTime = _messages.StringField(3)


class OidcConfig(_messages.Message):
  r"""OidcConfig holds the configuration for the OIDC provider that's used to
  authenticate users against a member.

  Enums:
    TokenEndpointRoutabilityValueValuesEnum: Connection method to be used when
      accessing the token endpoint.

  Messages:
    ExtraParametersValue: Additional parameters required by the Identity
      Provider

  Fields:
    aud: Audience claims to request when fetching the id_token - should
      include the --oidc-client-id configured for the cluster.
    authorizationEndpoint: Endpoint to be used for authentication of end user,
      ex. https://accounts.google.com/o/oauth2/v2/auth. See
      https://openid.net/specs/openid-connect-core-
      1_0.html#AuthorizationEndpoint
    clientId: Client Id for the OAuth client to be used when communicating
      with Identity Provider.
    clientSecret: Client Secret for the OAuth client to be used when
      communicating with Identity Provider.
    extraParameters: Additional parameters required by the Identity Provider
    issuer: Identity Provider that needs to issue tokens accepted by this
      cluster, ex. https://accounts.google.com. Should match the --oidc-
      issuer-url configured for the cluster.
    scopes: Scopes to be requested from Identity Provider
    tokenEndpoint: Endpoint to be used to obtain the id_token, ex.
      https://www.googleapis.com/oauth2/v4/token. See https://openid.net/specs
      /openid-connect-core-1_0.html#TokenEndpoint
    tokenEndpointRoutability: Connection method to be used when accessing the
      token endpoint.
  """

  class TokenEndpointRoutabilityValueValuesEnum(_messages.Enum):
    r"""Connection method to be used when accessing the token endpoint.

    Values:
      ENDPOINT_ROUTABILITY_UNSPECIFIED: Not set.
      PUBLIC: Identity Provider is available over internet
      GKE_CONNECT: Identity Provider is available On-Prem, use On-Prem proxy
        over GKE Connect.
    """
    ENDPOINT_ROUTABILITY_UNSPECIFIED = 0
    PUBLIC = 1
    GKE_CONNECT = 2

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ExtraParametersValue(_messages.Message):
    r"""Additional parameters required by the Identity Provider

    Messages:
      AdditionalProperty: An additional property for a ExtraParametersValue
        object.

    Fields:
      additionalProperties: Additional properties of type ExtraParametersValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ExtraParametersValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  aud = _messages.StringField(1, repeated=True)
  authorizationEndpoint = _messages.StringField(2)
  clientId = _messages.StringField(3)
  clientSecret = _messages.BytesField(4)
  extraParameters = _messages.MessageField('ExtraParametersValue', 5)
  issuer = _messages.StringField(6)
  scopes = _messages.StringField(7, repeated=True)
  tokenEndpoint = _messages.StringField(8)
  tokenEndpointRoutability = _messages.EnumField('TokenEndpointRoutabilityValueValuesEnum', 9)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('GoogleRpcStatus', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')