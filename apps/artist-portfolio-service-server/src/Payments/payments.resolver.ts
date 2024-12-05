import * as graphql from "@nestjs/graphql";
import { CheckCvvInput } from "../payments/CheckCvvInput";
import { VerifyCreditCardInput } from "../payments/VerifyCreditCardInput";
import { PaymentsService } from "./payments.service";

export class PaymentsResolver {
  constructor(protected readonly service: PaymentsService) {}

  @graphql.Query(() => String)
  async CheckCvv(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.CheckCvv(args);
  }

  @graphql.Mutation(() => String)
  async CheckCvvAction(
    @graphql.Args()
    args: CheckCvvInput
  ): Promise<string> {
    return this.service.CheckCvvAction(args);
  }

  @graphql.Query(() => String)
  async VerifyCreditCard(
    @graphql.Args()
    args: string
  ): Promise<string> {
    return this.service.VerifyCreditCard(args);
  }

  @graphql.Mutation(() => String)
  async VerifyCreditCardAction(
    @graphql.Args()
    args: VerifyCreditCardInput
  ): Promise<string> {
    return this.service.VerifyCreditCardAction(args);
  }
}
