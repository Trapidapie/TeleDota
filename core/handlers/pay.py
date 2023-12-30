from aiogram import Bot
from aiogram.types import Message, LabeledPrice, pre_checkout_query

from core.admin.settings import settings
from core.utils.command import send_hero_link

async def order(message: Message, bot: Bot, hero: str, item: str, price: int):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title=item.capitalize().replace('_', ' '),
        description=f"{item.capitalize().replace('_', ' ')} skin for \
        {hero.capitalize().replace('-', ' ')}",
        payload=item.capitalize().replace('_', ' '),
        provider_token=settings.bots.provider_token,
        currency='usd',
        prices=[
            LabeledPrice(
                label=item.capitalize().replace('_', ' '),
                amount=price
            ),
        ],
        max_tip_amount=500,  # Increased to cover all suggested tip amounts
        suggested_tip_amounts=[10, 20, 200, 500],
        start_parameter='test-payment',
        provider_data=None,
        photo_url=None,
        photo_size=None,
        photo_width=None,
        photo_height=None,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=True,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15,
    )


async def pre_checkout_q(pre_checkout_qu: pre_checkout_query.PreCheckoutQuery, bot: Bot):
    await pre_checkout_qu.answer(ok=True)

async def successful_payment(message: Message):
    msg = (f'Спасибо за покупку!\n {message.successful_payment.total_amount // 100}'
           f' {message.successful_payment.currency}.'
           f' \n\r Наш менеджер свяжется с вами в ближайшее время.')

    await message.answer(msg)