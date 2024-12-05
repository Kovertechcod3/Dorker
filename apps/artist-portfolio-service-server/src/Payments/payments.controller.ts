import * as common from "@nestjs/common";
import * as swagger from "@nestjs/swagger";
import * as errors from "../errors";
import { PaymentsService } from "./payments.service";
import { VerifyCreditCardInput } from "../payments/VerifyCreditCardInput";

@swagger.ApiTags("payments")
@common.Controller("payments")
export class PaymentsController {
  constructor(protected readonly service: PaymentsService) {}

  @common.Get("/:id/check-cvv")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async CheckCvv(
    @common.Body()
    body: VerifyCreditCardInput
  ): Promise<string> {
        return this.service.CheckCvv(body);
      }

  @common.Post("/check-cvv-action")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async CheckCvvAction(
    @common.Body()
    body: VerifyCreditCardInput
  ): Promise<string> {
        return this.service.CheckCvvAction(body);
      }

  @common.Get("/:id/verify-credit-card")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async VerifyCreditCard(
    @common.Body()
    body: VerifyCreditCardInput
  ): Promise<string> {
        return this.service.VerifyCreditCard(body);
      }

  @common.Post("/verify-cc-action")
  @swagger.ApiOkResponse({
    type: String
  })
  @swagger.ApiNotFoundResponse({
    type: errors.NotFoundException
  })
  @swagger.ApiForbiddenResponse({
    type: errors.ForbiddenException
  })
  async VerifyCreditCardAction(
    @common.Body()
    body: VerifyCreditCardInput
  ): Promise<string> {
        return this.service.VerifyCreditCardAction(body);
      }
}
